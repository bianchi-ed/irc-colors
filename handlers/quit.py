import datetime
from colorama import Fore, Style
import sys

def handle_quit(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    message = ' '.join(parts[2:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    
    colored_message = f"{Fore.LIGHTRED_EX}({timestamp}) {user} has quit: {message}{Fore.RESET}"
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)