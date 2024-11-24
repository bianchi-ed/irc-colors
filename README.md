![image](https://github.com/user-attachments/assets/ddc6fdf2-5e34-4a63-b49f-0fde344cac5f)

# IRC Colors

IRC-Colors is a minimalistic IRC client written in Python that runs on the terminal. The client connects to a single IRC server, joins multiple channels, and handles basic IRC commands/events with color-coded messages.

**This is a Work in Progress Project**

## Installation

1. Clone the repository and navigate to the directory:
    ```sh
    git clone https://github.com/bianchi-ed/irc-colors.git
    cd irc-colors
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Update the server configuration constants in `irc-colors.py` if necessary:
    ```python
    SERVER = "irc.libera.chat"
    PORT = 6667
    CHANNEL = "#targetchannel"
    NICKNAME = "yournickname"
    ```

2. Run the IRC client:
    ```sh
    python irc-colors.py
    ```

## Available Commands

### /join <channel>
- **Description**: Join a specified channel.
- **Usage**: `/join #python`
- **File**: [commands/join.py](commands/join.py)

### /leave <channel>
- **Description**: Leave a specified channel.
- **Usage**: `/leave #python`
- **File**: [commands/leave.py](commands/leave.py)

### /msg <target> <message>
- **Description**: Send a private message to a user or a message to a channel.
- **Usage**: `/msg username Hello there!` or `/msg #python Hello everyone!`
- **File**: [commands/msg.py](commands/msg.py)

### /quit <message>
- **Description**: Quit the IRC server with an optional message.
- **Usage**: `/quit Goodbye!`
- **File**: [commands/quit.py](commands/quit.py)

## Event Handlers

### JOIN
- **File**: [handlers/join.py](handlers/join.py)
- **Description**: Handles the event when a user joins a channel.
- **Color**: Light Green (`Fore.LIGHTGREEN_EX`)

### PART
- **File**: [handlers/part.py](handlers/part.py)
- **Description**: Handles the event when a user leaves a channel.
- **Color**: Light Red (`Fore.LIGHTRED_EX`)

### QUIT
- **File**: [handlers/quit.py](handlers/quit.py)
- **Description**: Handles the event when a user quits the IRC server.
- **Color**: Light Red (`Fore.LIGHTRED_EX`)

### PRIVMSG
- **File**: [handlers/privmsg.py](handlers/privmsg.py)
- **Description**: Handles private messages sent to a user or a channel.
- **Color**: Light Green (`Fore.LIGHTGREEN_EX`) for channel messages, Light Blue (`Fore.LIGHTBLUE_EX`) for private messages

### NOTICE
- **File**: [handlers/notice.py](handlers/notice.py)
- **Description**: Handles notice messages sent to a user or a channel.
- **Color**: Yellow (`Fore.YELLOW`)

### NICK
- **File**: [handlers/nick.py](handlers/nick.py)
- **Description**: Handles the event when a user changes their nickname.
- **Color**: Light Yellow (`Fore.LIGHTYELLOW_EX`)

### MODE
- **File**: [handlers/mode.py](handlers/mode.py)
- **Description**: Handles mode changes for a user or a channel.
- **Color**: Light Yellow (`Fore.LIGHTYELLOW_EX`)

## Numeric Responses Handlers

### 001 (RPL_WELCOME)
- **File**: [handlers/event_001.py](handlers/event_001.py)
- **Description**: Welcome message from the server.
- **Color**: Light Cyan (`Fore.LIGHTCYAN_EX`)

### 002 (RPL_YOURHOST)
- **File**: [handlers/event_002.py](handlers/event_002.py)
- **Description**: Information about the server host.
- **Color**: Light Cyan (`Fore.LIGHTCYAN_EX`)

### 003 (RPL_CREATED)
- **File**: [handlers/event_003.py](handlers/event_003.py)
- **Description**: Server creation date.
- **Color**: Light Cyan (`Fore.LIGHTCYAN_EX`)

### 004 (RPL_MYINFO)
- **File**: [handlers/event_004.py](handlers/event_004.py)
- **Description**: Server information.
- **Color**: Light Cyan (`Fore.LIGHTCYAN_EX`)

### 005 (RPL_BOUNCE)
- **File**: [handlers/event_005.py](handlers/event_005.py)
- **Description**: Server features.
- **Color**: White (`Fore.WHITE`)

### 250 (RPL_STATSCONN)
- **File**: [handlers/event_250.py](handlers/event_250.py)
- **Description**: Connection statistics.
- **Color**: Magenta (`Fore.MAGENTA`)

### 251 (RPL_LUSERCLIENT)
- **File**: [handlers/event_251.py](handlers/event_251.py)
- **Description**: Number of users and services.
- **Color**: Magenta (`Fore.MAGENTA`)

### 252 (RPL_LUSEROP)
- **File**: [handlers/event_252.py](handlers/event_252.py)
- **Description**: Number of IRC operators online.
- **Color**: Magenta (`Fore.MAGENTA`)

### 253 (RPL_LUSERUNKNOWN)
- **File**: [handlers/event_253.py](handlers/event_253.py)
- **Description**: Number of unknown connections.
- **Color**: Magenta (`Fore.MAGENTA`)

### 254 (RPL_LUSERCHANNELS)
- **File**: [handlers/event_254.py](handlers/event_254.py)
- **Description**: Number of channels formed.
- **Color**: Magenta (`Fore.MAGENTA`)

### 255 (RPL_LUSERME)
- **File**: [handlers/event_255.py](handlers/event_255.py)
- **Description**: Server connection summary.
- **Color**: Magenta (`Fore.MAGENTA`)

### 265 (RPL_LOCALUSERS)
- **File**: [handlers/event_265.py](handlers/event_265.py)
- **Description**: Local user information.
- **Color**: Magenta (`Fore.MAGENTA`)

### 266 (RPL_GLOBALUSERS)
- **File**: [handlers/event_266.py](handlers/event_266.py)
- **Description**: Global user information.
- **Color**: Magenta (`Fore.MAGENTA`)

### 353 (RPL_NAMREPLY)
- **File**: [handlers/event_353.py](handlers/event_353.py)
- **Description**: List of users in a channel.
- **Color**: Cyan (`Fore.CYAN`)

### 366 (RPL_ENDOFNAMES)
- **File**: [handlers/event_366.py](handlers/event_366.py)
- **Description**: End of NAMES list.
- **Color**: Black with Cyan Background (`Fore.BLACK`, `Back.CYAN`)

### 372 (RPL_MOTD)
- **File**: [handlers/event_372.py](handlers/event_372.py)
- **Description**: Message of the day.
- **Color**: Blue (`Fore.BLUE`)

### 375 (RPL_MOTDSTART)
- **File**: [handlers/event_375.py](handlers/event_375.py)
- **Description**: Start of the message of the day.
- **Color**: Black with Blue Background (`Fore.BLACK`, `Back.BLUE`)

### 376 (RPL_ENDOFMOTD)
- **File**: [handlers/event_376.py](handlers/event_376.py)
- **Description**: End of the message of the day.
- **Color**: Black with Blue Background (`Fore.BLACK`, `Back.BLUE`)