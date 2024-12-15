import datetime
from colorama import Fore, Style
import sys

def handle_event_263(response):
    parts = response.split(' ')
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    message = ' '.join(parts[3:])[1:]
    colored_message = f"{Fore.RED}[{timestamp}] [263] [RPL_TRYAGAIN] {message}{Style.RESET_ALL}"
    
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)