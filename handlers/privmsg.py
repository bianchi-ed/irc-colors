import sys
import datetime
from colorama import Fore, Style

def handle_privmsg(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    target = parts[2]
    message = ' '.join(parts[3:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    
    if target.startswith('#'):
        colored_message = f"{Fore.GREEN}[{timestamp}] [{target}] {user}: {message}{Fore.RESET}"
    else:
        colored_message = f"{Fore.MAGENTA}[{timestamp}] [PRIVMSG] {user}: {message}{Fore.RESET}"

    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)