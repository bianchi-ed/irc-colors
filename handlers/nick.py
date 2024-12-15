import datetime
from colorama import Fore, Style
import sys

def handle_nick(response):
    parts = response.split(' ')
    old_nick = parts[0].split('!')[0][1:]
    new_nick = parts[2][1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.LIGHTYELLOW_EX}[{timestamp}] [NICK] {old_nick} is now known as {new_nick}{Fore.RESET}"
    
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)