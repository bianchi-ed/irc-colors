import datetime
from colorama import Fore, Style
import sys

def handle_notice(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    target = parts[2]
    message = ' '.join(parts[3:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    
    colored_message = f"{Fore.YELLOW}[{timestamp}] [NOTICE] {user} to {target}: {message}{Style.RESET_ALL}"
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)