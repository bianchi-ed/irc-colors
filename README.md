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

