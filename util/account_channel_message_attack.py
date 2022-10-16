import threading
from urllib import response
import requests
import Hazard
import random

from time import sleep
from itertools import cycle
from colorama import Fore

from util.plugins.common import print_slow, setTitle, getheaders, proxy

def selector2(token, users):
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    while True:
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                for channel in channelIds:
                    requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',headers=headers,data={"content": f"{message_Content}"})
                    setTitle(f"Messaging "+channel['id'])
                print(f"{Fore.RED}Created groupchat")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Rate limited ({response.json()['retry_after']}ms){Fore.RESET}")
            else:
                print(f"{Fore.RED}Error: {response.status_code}{Fore.RESET}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    Hazard.main()

def randomizer(token, ID):
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                for channel in channelIds:
                    setTitle(f"Messaging "+channel['id'])
                print(f"{Fore.RED}Created groupchat")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Rate limited ({response.json()['retry_after']}ms){Fore.RESET}")
            else:
                print(f"{Fore.RED}Error: {response.status_code}{Fore.RESET}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    Hazard.main()


def channel_message(token,message_Content):
    print(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Do you want to choose user(s) yourself to groupchat spam or do you want to select randoms?')
    sleep(1)
    print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] choose user(s) yourself
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] randomize the users
                        ''')
    secondchoice = int(input(
        f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Second Choice: {Fore.RED}'))

    if secondchoice not in [1, 2]:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')
        sleep(1)
        Hazard.main()

    #if they choose to import the users manually
    if secondchoice == 1:
        setTitle(f"Creating groupchats")
        #if they choose specific users
        recipients = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Input the users you want to create a groupchat with (separate by , id,id2,id3): {Fore.RED}')
        user = recipients.split(',')
        if "," not in recipients:
            print(f"\n{Fore.RED}You didn't have any commas (,) format is id,id2,id3")
            sleep(3)
            Hazard.main()
        headers = {'Authorization': token}
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        print_slow("\"ctrl + c\" at anytime to stop\n")
        while True:
            for channel in channelIds:
                requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                headers=headers,
                data={"content": f"{message_Content}"})
                setTitle(f"Messaging "+channel['id'])
                print(f"{Fore.RED}Messaged ID: {Fore.WHITE}"+channel['id']+Fore.RESET)
                print(f"{Fore.RED}Created groupchat")
            else:
                sleep(1.5)
            selector2(token, user)

    #if they choose to randomize the selection
    elif secondchoice == 2:
        setTitle(f"Creating groupchats")
        IDs = []
        #Get all users to spam groupchats 
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        for friend in friendIds:
            IDs.append(friend['id'])
        headers = {'Authorization': token}
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        print_slow("\"ctrl + c\" at anytime to stop\n")
        while True:
            for channel in channelIds:
                requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                headers=headers,
                data={"content": f"{message_Content}"})
                setTitle(f"Messaging "+channel['id'])
                print(f"{Fore.RED}Messaged ID: {Fore.WHITE}"+channel['id']+Fore.RESET)
                print(f"{Fore.RED}Created groupchat")
            else:
                sleep(1.5)
    selector2(token, user)