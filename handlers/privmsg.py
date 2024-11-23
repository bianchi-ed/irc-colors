import datetime
from colorama import Fore, Style
import sys

def handle_privmsg(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    target = parts[2]
    message = ' '.join(parts[3:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    
    if target.startswith('#'):
        colored_message = f"{Fore.LIGHTGREEN_EX}[{timestamp}] [PRIVMSG] FROM {user} TO CHANNEL {target}: {message}{Fore.RESET}"
    else:
        colored_message = f"{Fore.MAGENTA}[{timestamp}] [PRIVMSG] FROM {user} TO YOU: {message}{Fore.RESET}"

    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)