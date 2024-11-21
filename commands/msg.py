from colorama import Fore
import datetime

def send_message(sock, target, message):
    sock.send(f"PRIVMSG {target} :{message}\r\n".encode('utf-8'))

def execute(client, parts):
    if len(parts) < 3:
        print("Usage: /msg <target> <message>")
    else:
        target = parts[1]
        message = parts[2]
        send_message(client.sock, target, message)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if target.startswith('#'):
            color = Fore.LIGHTGREEN_EX
        else:
            color = Fore.LIGHTBLUE_EX
        print(f"\033[F\033[K{color}({timestamp}) Message sent to {target}: {message}{Fore.RESET}")