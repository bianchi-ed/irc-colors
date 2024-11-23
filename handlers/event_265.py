import datetime
from colorama import Fore, Style
import sys

def handle_event_265(response):
    parts = response.split(' ')
    server_message = ' '.join(parts[3:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.MAGENTA}[{timestamp}] [265] [RPL_LOCALUSERS]: {server_message}{Fore.RESET}"
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)