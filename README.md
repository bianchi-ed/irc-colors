![image](https://github.com/user-attachments/assets/9dc6e509-3fb4-44c9-9339-ce904f3ffbf2)

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

4. Run the IRC client:
    ```sh
    python irc-colors.py
    ```

## Color Code

Under construction

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

### /disconnect <message>
- **Description**: Disconnect from the IRC server.
- **Usage**: `/disconnect`
- **File**: [commands/disconnect.py](commands/disconnect.py)

## Event Handlers

### JOIN
- **File**: [handlers/join.py](handlers/join.py)
- **Description**: Handles the event when a user joins a channel.

### PART
- **File**: [handlers/part.py](handlers/part.py)
- **Description**: Handles the event when a user leaves a channel.

### QUIT
- **File**: [handlers/quit.py](handlers/quit.py)
- **Description**: Handles the event when a user quits the IRC server.

### PRIVMSG
- **File**: [handlers/privmsg.py](handlers/privmsg.py)
- **Description**: Handles private messages sent to a user or a channel.

### NOTICE
- **File**: [handlers/notice.py](handlers/notice.py)
- **Description**: Handles notice messages sent to a user or a channel.

### NICK
- **File**: [handlers/nick.py](handlers/nick.py)
- **Description**: Handles the event when a user changes their nickname.

### MODE
- **File**: [handlers/mode.py](handlers/mode.py)
- **Description**: Handles mode changes for a user or a channel.

## Numeric Responses Handlers

### 001 (RPL_WELCOME)
- **File**: [handlers/event_001.py](handlers/event_001.py)
- **Description**: Welcome message from the server.

### 002 (RPL_YOURHOST)
- **File**: [handlers/event_002.py](handlers/event_002.py)
- **Description**: Information about the server host.

### 003 (RPL_CREATED)
- **File**: [handlers/event_003.py](handlers/event_003.py)
- **Description**: Server creation date.

### 004 (RPL_MYINFO)
- **File**: [handlers/event_004.py](handlers/event_004.py)
- **Description**: Server information.

### 005 (RPL_BOUNCE)
- **File**: [handlers/event_005.py](handlers/event_005.py)
- **Description**: Server features.

### 250 (RPL_STATSCONN)
- **File**: [handlers/event_250.py](handlers/event_250.py)
- **Description**: Connection statistics.

### 251 (RPL_LUSERCLIENT)
- **File**: [handlers/event_251.py](handlers/event_251.py)
- **Description**: Number of users and services.

### 252 (RPL_LUSEROP)
- **File**: [handlers/event_252.py](handlers/event_252.py)
- **Description**: Number of IRC operators online.

### 253 (RPL_LUSERUNKNOWN)
- **File**: [handlers/event_253.py](handlers/event_253.py)
- **Description**: Number of unknown connections.

### 254 (RPL_LUSERCHANNELS)
- **File**: [handlers/event_254.py](handlers/event_254.py)
- **Description**: Number of channels formed.

### 255 (RPL_LUSERME)
- **File**: [handlers/event_255.py](handlers/event_255.py)
- **Description**: Server connection summary.

### 265 (RPL_LOCALUSERS)
- **File**: [handlers/event_265.py](handlers/event_265.py)
- **Description**: Local user information.

### 266 (RPL_GLOBALUSERS)
- **File**: [handlers/event_266.py](handlers/event_266.py)
- **Description**: Global user information.

### 353 (RPL_NAMREPLY)
- **File**: [handlers/event_353.py](handlers/event_353.py)
- **Description**: List of users in a channel.

### 366 (RPL_ENDOFNAMES)
- **File**: [handlers/event_366.py](handlers/event_366.py)
- **Description**: End of NAMES list.

### 372 (RPL_MOTD)
- **File**: [handlers/event_372.py](handlers/event_372.py)
- **Description**: Message of the day.

### 375 (RPL_MOTDSTART)
- **File**: [handlers/event_375.py](handlers/event_375.py)
- **Description**: Start of the message of the day.

### 376 (RPL_ENDOFMOTD)
- **File**: [handlers/event_376.py](handlers/event_376.py)
- **Description**: End of the message of the day.

