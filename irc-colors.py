import socket
import threading
import importlib
from colorama import init, Fore, Style

init(autoreset=True)

# Server configuration constants
SERVER = "irc.libera.chat"
PORT = 6667
CHANNEL = "#testtest333"
NICKNAME = "yournickname"

def print_rainbow_ascii_art():
    ascii_art = r"""
 _                         _                              
(_)_ __ ___       ___ ___ | | ___  _ __ ___   _ __  _   _ 
| | '__/ __|____ / __/ _ \| |/ _ \| '__/ __| | '_ \| | | |
| | | | (_|_____| (_| (_) | | (_) | |  \__ \_| |_) | |_| |
|_|_|  \___|     \___\___/|_|\___/|_|  |___(_) .__/ \__, |
                                             |_|    |___/    
                         Thanks for using irc-colors.py :) 
                                              - bianchi-ed
    """
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i, line in enumerate(ascii_art.split('\n')):
        color = colors[i % len(colors)]
        print(color + line + Style.RESET_ALL)

print_rainbow_ascii_art()

class IRCClient:
    def __init__(self, server, port, channel, nickname):
        self.server = server
        self.port = port
        self.channel = channel
        self.nickname = nickname
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True

    def connect(self):
        self.sock.connect((self.server, self.port))
        self.sock.send(f"NICK {self.nickname}\r\n".encode('utf-8'))
        self.sock.send(f"USER {self.nickname} 0 * :{self.nickname}\r\n".encode('utf-8'))
        self.sock.send(f"JOIN {self.channel}\r\n".encode('utf-8'))

    def listen(self):
        buffer = ""
        while self.running:
            try:
                data = self.sock.recv(2048).decode('utf-8')
                if not data:
                    break
                buffer += data
                while '\r\n' in buffer:
                    line, buffer = buffer.split('\r\n', 1)
                    if line.startswith('PING'):
                        self.sock.send(f"PONG {line.split()[1]}\r\n".encode('utf-8'))
                    else:
                        handled = self.handle_event(line)
                        if not handled:
                            print(line)
            except ConnectionAbortedError:
                break

    def handle_event(self, response):
        #print(f"Received response: {response}")  # Debugging line
        parts = response.split()
        if len(parts) < 2:
            #print("Invalid response format")  # Debugging line
            return False
        event = parts[1].upper()
        #print(f"Extracted event: {event}")  # Debugging line
        try:
            if event.isdigit():
                handler_module = importlib.import_module(f'handlers.event_{event.lower()}')
                handler_function = getattr(handler_module, f'handle_event_{event.lower()}')
            else:
                handler_module = importlib.import_module(f'handlers.{event.lower()}')
                handler_function = getattr(handler_module, f'handle_{event.lower()}')
            handler_function(response)
            return True
        except ImportError as e:
            #print(f"Handler module not found for event: {event}, error: {e}")  # Debugging line
            return False
        except AttributeError as e:
            #print(f"Handler function not found for event: {event}, error: {e}")  # Debugging line
            return False

    def handle_input(self):
        while True:
            command = input()
            if command.startswith('/'):
                self.execute_command(command)

    def execute_command(self, command):
        parts = command[1:].split(' ', 2)
        command_name = parts[0]
        try:
            command_module = importlib.import_module(f'commands.{command_name}')
            command_function = getattr(command_module, 'execute')
            command_function(self, parts)
        except ImportError:
            print(f"Unknown command module: {command_name}")
        except AttributeError:
            print(f"Unknown command function: {command_name}")

if __name__ == "__main__":
    # Create IRC client instance and connect to server
    client = IRCClient(SERVER, PORT, CHANNEL, NICKNAME)
    client.connect()

    # Separate threads for listening and input handling
    listen_thread = threading.Thread(target=client.listen)
    input_thread = threading.Thread(target=client.handle_input)

    listen_thread.start()
    input_thread.start()

    listen_thread.join()
    input_thread.join()
