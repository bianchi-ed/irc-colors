from colorama import Fore
import datetime

def join_channel(sock, channel):
    sock.send(f"JOIN {channel}\r\n".encode('utf-8'))

def execute(client, parts):
    if len(parts) < 2:
        print("Usage: /join <channel>")
    else:
        channel = parts[1]
        join_channel(client.sock, channel)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\033[F\033[K{Fore.LIGHTGREEN_EX}({timestamp}) Joined channel {channel}{Fore.RESET}")