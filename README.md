# IRC Colors

IRC-Colors is a minimalistic IRC client writen in Python. The client connects to a single IRC server. 

This is a python study project.

## Features

- Connect to a single IRC server and join multiple channels.
- Send and receive messages.
- Handle basic IRC commands.
- Handle common IRC events.

## Color Coding
- **Light Green** (`Fore.LIGHTGREEN_EX`): Indicates successful receiving/sending messages in channels.
- **Light Red** (`Fore.LIGHTRED_EX`): Indicates actions such as leaving a channel or quitting the IRC server/client.
- **Light Yellow** (`Fore.LIGHTYELLOW_EX`): Indicates nickname changes and NOTICE messages.
- **Light Blue** (`Fore.LIGHTBLUE_EX`): Indicates private messages exchange.
- **Cyan** (`Fore.CYAN`): Indicates users joining channels.
- White messages are messages that are probably dont have a handler yet.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bianchi-ed/irc-colors.git
    cd irc-colors
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

##Usage

1. Update the server configuration constants in `main.py` if necessary:
    ```python
    SERVER = "irc.libera.chat"
    PORT = 6667
    CHANNEL = "#python"
    NICKNAME = "beginnerdev"
    ```

2. Run the IRC client:
    ```sh
    python main.py
    ```

3. Use the following commands in the client:
    - `/join <channel>`: Join a specified channel
    - `/leave <channel>`: Leave a specified channel
    - `/msg <target> <message>`: Send a private message to a user or a message to a channel
    - `/quit <message>`: Quit the IRC server with an optional message

##Directory Structure

project/
├── commands/                # Directory for IRC command implementations
│   ├── __init__.py
│   ├── join.py              # Command to join a channel
│   ├── leave.py             # Command to leave a channel
│   ├── msg.py               # Command to send a message
│   ├── quit.py              # Command to quit the IRC server and client
├── handlers/                # Directory for IRC event handlers
│   ├── __init__.py
│   ├── join.py              # Handler for join events
│   ├── nick.py              # Handler for nickname change events
│   ├── notice.py            # Handler for notice events
│   ├── part.py              # Handler for part events
│   ├── privmsg.py           # Handler for private message events
│   ├── quit.py              # Handler for quit events
├── main.py                  # Main entry point of the IRC client
├── read.me                  # Project documentation
└── requirements.txt         # Project dependencies
