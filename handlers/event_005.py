import datetime
from colorama import Fore, Style
import sys

def handle_event_005(response):
    parts = response.split(' ')
    server_features = ' '.join(parts[3:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.WHITE}[{timestamp}] [005] [RPL_BOUNCE]: {server_features}{Fore.RESET}"
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)