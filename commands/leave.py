from colorama import Fore
import datetime

def part_channel(sock, channel):
    sock.send(f"PART {channel}\r\n".encode('utf-8'))

def execute(client, parts):
    if len(parts) < 2:
        print("Usage: /part <channel>")
    else:
        channel = parts[1]
        part_channel(client.sock, channel)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')