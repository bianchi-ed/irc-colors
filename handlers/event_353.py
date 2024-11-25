import datetime
from colorama import Fore, Style
import sys

def handle_event_353(response):
    parts = response.split(' ')
    channel = parts[4]
    users = ' '.join(parts[5:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    
    # Split users into multiple lines with a semicolon separator
    max_users_per_line = 10
    user_list = users.split(' ')
    user_lines = ['; '.join(user_list[i:i + max_users_per_line]) for i in range(0, len(user_list), max_users_per_line)]
    
    # Print each line with the desired formatting
    for line in user_lines:
        colored_message = f"{Fore.GREEN}[{timestamp}] [353] [RPL_NAMREPLY]: {channel} : {line}{Style.RESET_ALL}"
        sys.stdout.write(colored_message + '\n')
    
    sys.stdout.write(Style.RESET_ALL)