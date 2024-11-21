# IRC Colors
IRC-Colors is a minimalistic IRC client written in Python that runs on the terminal. The client is able to connect to a single IRC server, join multiple channels, and handle basic IRC commands/events. It uses different colors to display various types of information.

This is a python study project.

## Color Coding
- **Light Green** (`Fore.LIGHTGREEN_EX`): Indicates successful receiving/sending messages in channels.
- **Light Red** (`Fore.LIGHTRED_EX`): Indicates actions such as leaving a channel or quitting the IRC server/client.
- **Light Yellow** (`Fore.LIGHTYELLOW_EX`): Indicates nickname changes and NOTICE messages.
- **Light Blue** (`Fore.LIGHTBLUE_EX`): Indicates private messages exchange.
- **Cyan** (`Fore.CYAN`): Indicates users joining channels.
- White messages are messages that dont have a handler implemented yet.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bianchi-ed/irc-colors.git
    cd irc-colors
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    ```

    ```sh
    venv\Scripts\activate
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Update the server configuration constants in `main.py` if necessary:
    ```python
    SERVER = "irc.libera.chat"
    PORT = 6667
    CHANNEL = "#targetchannel"
    NICKNAME = "yournickname"
    ```

2. Run the IRC client:
    ```sh
    python main.py
    ```

## Available Commands

- **`/join <channel>`**
    - **Description**: Join a specified channel.
    - **Usage**: `/join #python`
  
- **`/leave <channel>`**
    - **Description**: Leave a specified channel.
    - **Usage**: `/leave #python`
  
- **`/msg <target> <message>`**
    - **Description**: Send a private message to a user or a message to a channel.
    - **Usage**: `/msg username Hello there!` or `/msg #python Hello everyone!`
  
- **`/quit <message>`**
    - **Description**: Quit the IRC server with an optional message.
    - **Usage**: `/quit Goodbye!`
