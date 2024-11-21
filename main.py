import socket
import threading
import importlib
from colorama import init, Fore

init(autoreset=True)

# Server configuration constants
SERVER = "irc.libera.chat"
PORT = 6667
CHANNEL = "#python"
NICKNAME = "beginnerdev"

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
        while self.running:
            try:
                response = self.sock.recv(2048).decode('utf-8')
                if response.startswith('PING'):
                    self.sock.send(f"PONG {response.split()[1]}\r\n".encode('utf-8'))
                else:
                    handled = self.handle_event(response)
                    if not handled:
                        print(response)
            except ConnectionAbortedError:
                break

    def handle_event(self, response):
        event = response.split()[1].upper()
        try:
            handler_module = importlib.import_module(f'handlers.{event.lower()}')
            handler_function = getattr(handler_module, f'handle_{event.lower()}')
            handler_function(response)
            return True
        except (ImportError, AttributeError):
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