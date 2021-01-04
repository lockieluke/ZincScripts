import os
import shutil
import platform
from colorama import Fore, init
from typing import List
from paths import asarPath, javaPath, appBuildPath, nativeJarPath, nodeModulePath

from utils import rmfiles, rmdir

if not platform.system() == "Windows":
    print("Build script is currently not supported for other platforms due to the lack of fund for purchasing "
          "machines with other platforms for development")
    exit(1)
    pass

init(convert=True)

if os.path.exists(appBuildPath):
    print(Fore.RED + "Build already exists, remove previous builds to continue" + Fore.RESET)
    exit(1)
    pass

unnecessaryFolders: List[str] = [".cache", '.idea', 'main', 'scripts', 'window']
unnecessaryFiles: List[str] = [".eslintignore", '.eslintrc.json', '.gitignore', '.gitmodules', '.prettierignore',
                               '.prettierrc.json', 'devLicense.json', 'index.ts', 'README.md', 'tsconfig.json']
unnecessaryModules: List[str] = ["typescript"]

print("Checking source code...")
if not os.path.exists(os.path.join(os.getcwd(), "java")):
    print("OpenJDK for Zinc Native not found, follow guide on GitHub to see how you can download it")
    pass
print("Starting build...")
buildProc = os.popen('yarn build-win')
buildProc.read()
print(Fore.GREEN + "Finished building Zinc and now constructing Zinc Native directories..." + Fore.RESET)
shutil.move(javaPath, os.path.join(appBuildPath, "java"))
shutil.move(nativeJarPath, os.path.join(appBuildPath, "native"))
print(Fore.GREEN + "Removing unnecessary files from app assets..." + Fore.RESET)
rmdir(unnecessaryFolders, asarPath)
rmfiles(unnecessaryFiles, asarPath)
print(Fore.GREEN + "Removing unnecessary node modules from app assets..." + Fore.RESET)
rmdir(unnecessaryModules, nodeModulePath)
print(Fore.GREEN + "Packing app asset into asar format..." + Fore.RESET)
asarProc = os.popen('yarn asar ' + asarPath + ' ' + asarPath + '.asar')
asarProc.read()
print("Removing unpacked app assets...")
shutil.rmtree(asarPath)

print(Fore.GREEN + "DONE" + Fore.RESET)
