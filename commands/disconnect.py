from colorama import Fore
import datetime

def quit_connection(client, message="Goodbye!"):
    client.running = False
    client.sock.send(f"QUIT :{message}\r\n".encode('utf-8'))
    client.sock.close()

def execute(client, parts):
    message = "Goodbye!"
    if len(parts) > 1:
        message = " ".join(parts[1:])
    quit_connection(client, message)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\033[F\033[K{Fore.LIGHTRED_EX}({timestamp}) Disconnected: {message}{Fore.RESET}")
    client.stop()