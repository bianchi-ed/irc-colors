import datetime
from colorama import Fore 

def handle_notice(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    target = parts[2]
    message = ' '.join(parts[3:])[1:]
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    colored_message = f"{Fore.LIGHTYELLOW_EX}({timestamp}) NOTICE from @{user} to {target}: {message}{Fore.RESET}"
    print(colored_message, end='')