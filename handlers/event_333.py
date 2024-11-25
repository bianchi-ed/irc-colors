import datetime
from colorama import Fore, Back, Style
import sys

def handle_event_333(response):
    parts = response.split(' ')
    channel = parts[3]
    topic_setter = parts[4]
    topic_set_time = datetime.datetime.fromtimestamp(int(parts[5])).strftime('%Y-%m-%d %H:%M:%S')
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    colored_message = f"{Fore.BLACK}{Back.GREEN}[{timestamp}] [333] [RPL_TOPICWHOTIME]: Channel: {channel}, Topic set by: {topic_setter} at {topic_set_time}{Style.RESET_ALL}"
    sys.stdout.write(colored_message + '\n')
    sys.stdout.write(Style.RESET_ALL)