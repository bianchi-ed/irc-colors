import datetime
from colorama import Fore, Style
import sys

def handle_event_322(response):
    parts = response.split('\n')
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    
    channels = []
    for part in parts:
        if part.startswith(':'):
            channel_info = part.split(' ')[3:]
            channels.append(' '.join(channel_info))
    
    max_channels_per_line = 1
    channel_lines = ['; '.join(channels[i:i + max_channels_per_line]) for i in range(0, len(channels), max_channels_per_line)]

    for line in channel_lines:
        colored_message = f"{Fore.BLUE}[{timestamp}] [322] [RPL_LIST]: {line}{Style.RESET_ALL}"
        sys.stdout.write(colored_message + '\n')
    
    sys.stdout.write(Style.RESET_ALL)