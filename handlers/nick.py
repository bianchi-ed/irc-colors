import datetime
from colorama import Fore

def handle_nick(response):
    parts = response.split(' ')
    old_nick = parts[0].split('!')[0][1:]
    new_nick = parts[2][1:]
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.LIGHTYELLOW_EX}({timestamp}) @{old_nick} is now known as @{new_nick}{Fore.RESET}"
    print(colored_message, end='')