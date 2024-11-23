import datetime
from colorama import Fore, Back, Style
import sys

def handle_event_366(response):
    parts = response.split(' ')
    channel = parts[3]
    end_of_names_message = ' '.join(parts[4:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    colored_message = f"{Back.CYAN}{Fore.BLACK}[{timestamp}] [366] [RPL_ENDOFNAMES]: {channel} : {end_of_names_message}{Style.RESET_ALL}"
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)