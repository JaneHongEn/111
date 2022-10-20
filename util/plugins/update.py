# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import os
import shutil
import re
import sys

from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore
from util.plugins.common import clear, print_slow, setTitle, getheaders, THIS_VERSION
from util.plugins.common import *

def search_for_updates():
    clear()
    setTitle("Hazard Nuker Checking For Updates. . .")
    soup = BeautifulSoup(requests.get("https://github.com/JaneHongEn/111/tree/Hazard-Nuker-main").text, 'html.parser')
    for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
    setTitle("Hazard Nuker New Update Found!")
    print(f'''{Fore.YELLOW}
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                              {Fore.RED}Looks like this Hazard Nuker {THIS_VERSION} is outdated '''.replace('█', f'{Fore.WHITE}█{Fore.RED}'), end="\n\n")
    choice = str(input(
            f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}You want to update to the latest version? (Y to update): {Fore.RED}'))

    if choice.upper() == 'Y':
            print(f"{Fore.WHITE}\nUpdating. . .")
            setTitle(f'Hazard Nuker Updating...')
            #if they are running hazard.exe
            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("HazardNuker.zip", 'wb')as zipfile:
                    zipfile.write(new_version.content)
                with ZipFile("HazardNuker.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("HazardNuker.zip")
                try:
                    cwd = os.getcwd()+'\\HazardNuker\\'
                    shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), 'HazardNuker.exe')
                    shutil.copyfile(cwd+'README.md', 'README.md')                   
                    shutil.rmtree('HazardNuker')
                    setTitle('Hazard Nuker Update Complete!')
                    print(f"{Fore.GREEN}Update Successfully Finished!")
                    sleep(1)
                    sys.exit()
                except PermissionError as err:
                    clear()
                    print(f"{Fore.RED}\nHazard Nuker-{THIS_VERSION} doesn't have enough permission to update\ntry re-running again as admin or turn off anti-virus otherwise try and download it manually here {update_url}\n\n\"{err}\"")
                    sleep(10)
            #if they are running hazard source code
            else:
                new_version_soure = requests.get("https://drive.google.com/uc?id=1WRKwy6yhujsaozahWpTT5p-MQVdKgHbo&export=download")
                with open("Hazard-Nuker-master.zip", 'wb')as zipfile:
                    zipfile.write(new_version_soure.content)
                with ZipFile("Hazard-Nuker-master.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Hazard-Nuker-master.zip")
                try:
                    cwd = os.getcwd()+'\\111-Hazard-Nuker-main'
                    shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                    shutil.rmtree(cwd)
                    setTitle('Hazard Nuker Update Complete!')
                    print(f"{Fore.GREEN}Update Successfully Finished!")
                    sleep(1)
                except PermissionError as err:
                    clear()
                    print(f"{Fore.RED}\nHazard Nuker-{THIS_VERSION} doesn't have enough permission to update\ntry re-running again as admin or turn off anti-virus otherwise try and download it manually here {update_url}\n\n\"{err}\"")
                    sleep(10)

    else:
        input
        return
