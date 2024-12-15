import datetime
from colorama import Fore, Back, Style
import sys

def handle_event_470(response):
    parts = response.split(' ')
    original_channel = parts[3]
    new_channel = parts[4]
    server_message = ' '.join(parts[5:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.LIGHTYELLOW_EX}[{timestamp}] [470] [ERR_LINKCHANNEL] [{original_channel} -> {new_channel}] {server_message}{Style.RESET_ALL}"
    
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)