import os
import platform
import sys
import shutil
from typing import List
from colorama import Fore, init


def get_size(start_path='.') -> int:
    total_size: int = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp: str = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


buildJDKcmd: str = 'jlink --verbose --no-header-files --no-man-pages --compress=2 --strip-debug --add-modules="jdk.unsupported,java.sql,java.desktop,java.naming,java.management,java.instrument,java.security.jgss" --output="./java"'
jdkPath: str = os.path.join(os.getcwd(), 'java')

if not platform.system() == "Windows":
    print("JDK script is currently not supported for other platforms due to the lack of fund for purchasing "
          "machines with other platforms for development")
    exit(1)
    pass

init(convert=True)

print("Checking if JDK is installed...")
javaPath: str = os.popen("where java").readlines()[0].split('\n')[0]
javaVersion: str = os.popen("java --version").readlines()[0].split('\n')[0]
if os.path.exists(javaPath):
    print(
        Fore.GREEN + "Found Java!  Java was installed at " + javaPath + " which is on version " + javaVersion + Fore.RESET)
    pass
else:
    print(Fore.RED + "Java was not installed or not found.  If you are sure that you have installed Java, "
                     "please check if you "
                     "have added it into your PATH.", Fore.RESET)
    exit(1)
    pass
print("Checking if JLink exists...")
if os.path.exists(os.path.join(os.path.dirname(javaPath), 'jlink.exe')):
    print("JLink was found")
    pass
else:
    print("JLink was not found, please check that you have the correct installation of JDK which includes JLink by "
          "default.")
    pass

if os.path.exists(jdkPath) and not '--overwrite' in sys.argv:
    print("Building JDK will replace the previous java folder, please remove it before proceeding")
    exit(1)
    pass
elif '--overwrite' in sys.argv and os.path.exists(jdkPath):
    print("Removing previous JDK build because --overwrite flag was added")
    shutil.rmtree(jdkPath)
    pass

print("Building JDK...")
jlinkProc = os.popen(buildJDKcmd)
jlinkProc.read()
if not os.path.exists(jdkPath):
    print(Fore.RED + "Failed to build JDK" + Fore.RESET)
    exit(1)
    pass
print(Fore.GREEN + "Finished building JDK" + Fore.RESET)
print("Removing unnecessary files from the JDK")
rmdirs: List[str] = os.listdir(jdkPath)
for directory in rmdirs:
    if directory == 'bin' or directory == 'lib' or directory == 'release':
        rmdirs.remove(directory)
        pass
    pass
pass

rmdirs.remove('release')
shutil.rmtree(os.path.join(jdkPath, 'conf'))
shutil.rmtree(os.path.join(jdkPath, 'legal'))
os.remove(os.path.join(jdkPath, 'release'))
print("Build size is approximately " + str(round(get_size(jdkPath) / 1024 / 1024)) + " megabytes")

print(Fore.GREEN + "DONE" + Fore.RESET)
