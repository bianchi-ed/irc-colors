import datetime
from colorama import Fore, Back, Style
import sys

def handle_event_376(response):
    parts = response.split(' ')
    server_message = ' '.join(parts[3:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.BLACK}{Back.BLUE}[{timestamp}] [376] [RPL_ENDOFMOTD]: {server_message}{Style.RESET_ALL}"
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)