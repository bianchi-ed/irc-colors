import datetime
from colorama import Fore

def handle_part(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    channel = parts[2]
    message = ' '.join(parts[3:])[1:] if len(parts) > 3 else ''
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    colored_message = f"{Fore.LIGHTRED_EX}({timestamp}) @{user} has left {channel}: {message}{Fore.RESET}"
    print(colored_message, end='')