import datetime
from colorama import Fore, Style
import sys

def handle_join(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    channel = parts[2]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.LIGHTGREEN_EX}[{timestamp}] [JOIN] {user} has joined {channel}{Style.RESET_ALL}"
    
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)