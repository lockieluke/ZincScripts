from colorama import Fore
import requests
import os

download_url: str = 'https://download.java.net/java/GA/jdk15.0.1/51f4f36ad4ef43e39d0dfdbaf6549e32/9/GPL/openjdk-15.0.1_windows-x64_bin.zip'

print(Fore.WHITE + "Attempting to download the latest OpenJDK for Zinc Native" + Fore.RESET)
r = requests.get(download_url, allow_redirects=True)
open(os.path.join(os.getcwd(), 'java', 'java.zip'), 'wb').write(r.content)
