from colorama import Fore
import datetime

def request_channel_list(sock):
    sock.send("LIST\r\n".encode('utf-8'))

def execute(client, parts):
    request_channel_list(client.sock)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\033[F\033[K{Fore.BLUE}({timestamp}) Requested channel list{Fore.RESET}")