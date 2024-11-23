import datetime
from colorama import Fore, Style
import sys

def handle_mode(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    target = parts[2]
    message = ' '.join(parts[3:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    
    colored_message = f"{Fore.LIGHTYELLOW_EX}[{timestamp}] [MODE] {user} to {target}: {message}{Fore.RESET}"
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)