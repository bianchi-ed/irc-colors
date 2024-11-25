import datetime
from colorama import Fore, Back, Style
import sys

def handle_event_332(response):
    parts = response.split(' ')
    channel = parts[3]
    topic = ' '.join(parts[4:])[1:]
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.BLACK}{Back.GREEN}[{timestamp}] [332] [RPL_TOPIC]: Channel: {channel}, Topic: {topic}{Style.RESET_ALL}"
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)