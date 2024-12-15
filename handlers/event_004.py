import datetime
from colorama import Fore, Style
import sys

def handle_event_004(response):
    parts = response.split(' ')
    server_info = ' '.join(parts[3:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.LIGHTCYAN_EX}[{timestamp}] [004] [RPL_MYINFO] {server_info}{Fore.RESET}"
    
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)