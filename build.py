import subprocess
from colorama import Fore, init

init(convert=True)

proc: subprocess = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate(b"yarn run build")
print(str(stdout))
print(Fore.RED + str(stderr) + Fore.RESET)
