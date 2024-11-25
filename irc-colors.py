import socket
import threading
import importlib
from colorama import init, Fore, Back, Style
import random
import ssl

init(autoreset=True)

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
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX]
    random.shuffle(colors)
    for i, line in enumerate(ascii_art.split('\n')): 
        color = colors[i % len(colors)]
        print(color + line + Style.RESET_ALL)

class IRCClient:
    def __init__(self, server, port, channel, nickname, use_tls=False):
        self.server = server
        self.port = port
        self.channel = channel
        self.nickname = nickname
        self.use_tls = use_tls
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True

    def connect(self):
        try:
            if self.use_tls:
                context = ssl.create_default_context()
                self.sock = context.wrap_socket(self.sock, server_hostname=self.server)
            self.sock.connect((self.server, self.port))
            self.sock.send(f"NICK {self.nickname}\r\n".encode('utf-8'))
            self.sock.send(f"USER {self.nickname} 0 * :{self.nickname}\r\n".encode('utf-8'))
            self.sock.send(f"JOIN {self.channel}\r\n".encode('utf-8'))
            return True
        except (socket.error, socket.gaierror) as e:
            print(Fore.BLACK + Back.RED + f"Connection error: {e}" + Style.RESET_ALL)
            return False

    def listen(self):
        buffer = ""
        while self.running:
            try:
                data = self.sock.recv(2048).decode('utf-8', errors='replace')
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
            except Exception as e:
                print(f"Error: {e}")
                break

    def handle_event(self, response):
        parts = response.split()
        if len(parts) < 2:
            return False
        event = parts[1].upper()
        try:
            if event.isdigit():
                handler_module = importlib.import_module(f'handlers.event_{event.lower()}')
                handler_function = getattr(handler_module, f'handle_event_{event.lower()}')
            else:
                handler_module = importlib.import_module(f'handlers.{event.lower()}')
                handler_function = getattr(handler_module, f'handle_{event.lower()}')
            handler_function(response)
            return True
        except ImportError:
            return False
        except AttributeError:
            return False

    def handle_input(self):
        while self.running:
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

    def stop(self):
        self.running = False
        self.sock.close()

def main_menu():
    while True:
        print_rainbow_ascii_art()
        print(Fore.LIGHTCYAN_EX + "1. Connect to a server (TLS)" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "2. Connect to a server (Non-TLS)" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "3. Close Application" + Style.RESET_ALL)
        choice = input(Fore.LIGHTCYAN_EX + "\nEnter your choice: " + Style.RESET_ALL)
        
        if choice in ['1', '2']:
            server = input(Fore.LIGHTCYAN_EX + "Enter the server: " + Style.RESET_ALL)
            port = int(input(Fore.LIGHTCYAN_EX + "Enter the port: " + Style.RESET_ALL))
            channel = input(Fore.LIGHTCYAN_EX + "Enter the channel: " + Style.RESET_ALL)
            nickname = input(Fore.LIGHTCYAN_EX + "Enter your nickname: " + Style.RESET_ALL)
            use_tls = choice == '1'

            # Create IRC client instance and connect to server
            client = IRCClient(server, port, channel, nickname, use_tls)
            if client.connect():
                # Separate threads for listening and input handling
                listen_thread = threading.Thread(target=client.listen)
                input_thread = threading.Thread(target=client.handle_input)

                listen_thread.start()
                input_thread.start()

                listen_thread.join()
                input_thread.join()
            else:
                print(Fore.BLACK + Back.RED + "Failed to connect to the server. Please check your details and try again." + Style.RESET_ALL)
        elif choice == '3':
            print(Fore.RED + "Quitting..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()