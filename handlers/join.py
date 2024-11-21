import datetime
from colorama import Fore

def handle_join(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    channel = parts[2]
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.CYAN}({timestamp}) @{user} has joined {channel}{Fore.RESET}"
    print(colored_message, end='')