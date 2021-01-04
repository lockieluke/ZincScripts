import os

appBuildPath: str = os.path.join(os.getcwd(), "builds", "Zinc-win32-x64")
resourcesPath: str = os.path.join(appBuildPath, "resources")
asarPath: str = os.path.join(resourcesPath, "app")
nodeModulePath: str = os.path.join(asarPath, "node_modules")
javaPath: str = os.path.join(asarPath, "java")
nativeJarPath: str = os.path.join(asarPath, "native")