import os
from colorama import Fore, Style, init

print("Building...")
print(os.popen('cd ' + os.getcwd() + ' && cd .. && tsc').readline())
print(Fore.GREEN + "Build Succeeded" + Fore.RESET)