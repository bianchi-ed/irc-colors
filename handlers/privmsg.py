import datetime
from colorama import Fore

def handle_privmsg(response):
    parts = response.split(' ')
    user = parts[0].split('!')[0][1:]
    target = parts[2]
    message = ' '.join(parts[3:])[1:]
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if target.startswith('#'):
        # Message to a channel
        colored_message = f"{Fore.LIGHTGREEN_EX}({timestamp}) from @{user} on {target}: {message}{Fore.RESET}"
    else:
        # Private message
        colored_message = f"{Fore.LIGHTBLUE_EX}({timestamp}) from @{user}: {message}{Fore.RESET}"

    print(colored_message, end='')