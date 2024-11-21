import datetime
from colorama import Fore

def handle_quit(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    message = ' '.join(parts[2:])[1:]
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    colored_message = f"{Fore.LIGHTRED_EX}({timestamp}) @{user} has quit: {message}{Fore.RESET}"
    print(colored_message, end='')