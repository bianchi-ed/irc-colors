![image](https://github.com/user-attachments/assets/d05a7477-d74b-494c-bd43-9f238f4d1694)

# IRC Colors

IRC-Colors is a minimalistic IRC client written in Python that runs on the terminal. The client is able to connect to a single IRC server, join multiple channels, and handle basic IRC commands/events. It uses different colors to display various types of information.

This is a python study project.

## Installation

1. Clone the repository and navigate to the directory:
    ```sh
    git clone https://github.com/bianchi-ed/irc-colors.git
    ```

    ```sh
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

<details>
  <summary><strong>/join &lt;channel&gt;</strong></summary>
  
  - **Description**: Join a specified channel.
  - **Usage**: `/join #python`
  - **File**: [commands/join.py](commands/join.py)
  - **Function**: [`execute`](commands/join.py)
</details>

<details>
  <summary><strong>/leave &lt;channel&gt;</strong></summary>
  
  - **Description**: Leave a specified channel.
  - **Usage**: `/leave #python`
  - **File**: [commands/leave.py](commands/leave.py)
  - **Function**: [`execute`](commands/leave.py)
</details>

<details>
  <summary><strong>/msg &lt;target&gt; &lt;message&gt;</strong></summary>
  
  - **Description**: Send a private message to a user or a message to a channel.
  - **Usage**: `/msg username Hello there!` or `/msg #python Hello everyone!`
  - **File**: [commands/msg.py](commands/msg.py)
  - **Function**: [`execute`](commands/msg.py)
</details>

<details>
  <summary><strong>/quit &lt;message&gt;</strong></summary>
  
  - **Description**: Quit the IRC server with an optional message.
  - **Usage**: `/quit Goodbye!`
  - **File**: [commands/quit.py](commands/quit.py)
  - **Function**: [`execute`](commands/quit.py)
</details>
 

## Event Handlers

The IRC client includes handlers for various IRC events and responses. Each handler is responsible for processing a specific type of event and displaying a color-coded message in the terminal.

<details>
<summary>JOIN</summary>

- **File**: [handlers/join.py](handlers/join.py)
- **Description**: Handles the event when a user joins a channel.
- **Color**: Light Green (`Fore.LIGHTGREEN_EX`)

</details>

<details>
<summary>PART</summary>

- **File**: [handlers/part.py](handlers/part.py)
- **Description**: Handles the event when a user leaves a channel.
- **Color**: Light Red (`Fore.LIGHTRED_EX`)

</details>

<details>
<summary>QUIT</summary>

- **File**: [handlers/quit.py](handlers/quit.py)
- **Description**: Handles the event when a user quits the IRC server.
- **Color**: Light Red (`Fore.LIGHTRED_EX`)

</details>

<details>
<summary>PRIVMSG</summary>

- **File**: [handlers/privmsg.py](handlers/privmsg.py)
- **Description**: Handles private messages sent to a user or a channel.
- **Color**: Light Green (`Fore.LIGHTGREEN_EX`) for channel messages, Light Blue (`Fore.LIGHTBLUE_EX`) for private messages

</details>

<details>
<summary>NOTICE</summary>

- **File**: [handlers/notice.py](handlers/notice.py)
- **Description**: Handles notice messages sent to a user or a channel.
- **Color**: Yellow (`Fore.YELLOW`)

</details>

<details>
<summary>NICK</summary>

- **File**: [handlers/nick.py](handlers/nick.py)
- **Description**: Handles the event when a user changes their nickname.
- **Color**: Light Yellow (`Fore.LIGHTYELLOW_EX`)

</details>

<details>
<summary>MODE</summary>

- **File**: [handlers/mode.py](handlers/mode.py)
- **Description**: Handles mode changes for a user or a channel.
- **Color**: Light Yellow (`Fore.LIGHTYELLOW_EX`)

</details>

<details>
<summary>Numeric Responses</summary>

- **001 (RPL_WELCOME)**: [handlers/event_001.py](handlers/event_001.py)
- **002 (RPL_YOURHOST)**: [handlers/event_002.py](handlers/event_002.py)
- **003 (RPL_CREATED)**: [handlers/event_003.py](handlers/event_003.py)
- **004 (RPL_MYINFO)**: [handlers/event_004.py](handlers/event_004.py)
- **005 (RPL_BOUNCE)**: [handlers/event_005.py](handlers/event_005.py)
- **250 (RPL_STATSCONN)**: [handlers/event_250.py](handlers/event_250.py)
- **251 (RPL_LUSERCLIENT)**: [handlers/event_251.py](handlers/event_251.py)
- **252 (RPL_LUSEROP)**: [handlers/event_252.py](handlers/event_252.py)
- **253 (RPL_LUSERUNKNOWN)**: [handlers/event_253.py](handlers/event_253.py)
- **254 (RPL_LUSERCHANNELS)**: [handlers/event_254.py](handlers/event_254.py)
- **255 (RPL_LUSERME)**: [handlers/event_255.py](handlers/event_255.py)
- **265 (RPL_LOCALUSERS)**: [handlers/event_265.py](handlers/event_265.py)
- **266 (RPL_GLOBALUSERS)**: [handlers/event_266.py](handlers/event_266.py)
- **353 (RPL_NAMREPLY)**: [handlers/event_353.py](handlers/event_353.py)
- **366 (RPL_ENDOFNAMES)**: [handlers/event_366.py](handlers/event_366.py)
- **372 (RPL_MOTD)**: [handlers/event_372.py](handlers/event_372.py)
- **375 (RPL_MOTDSTART)**: [handlers/event_375.py](handlers/event_375.py)
- **376 (RPL_ENDOFMOTD)**: [handlers/event_376.py](handlers/event_376.py)

Each numeric response handler processes a specific server message and displays it with a unique color:
- **Light Cyan (`Fore.LIGHTCYAN_EX`)**: 001, 002, 003, 004
- **White (`Fore.WHITE`)**: 005
- **Magenta (`Fore.MAGENTA`)**: 250, 251, 252, 253, 254, 255, 265, 266
- **Cyan (`Fore.CYAN`)**: 353
- **Blue (`Fore.BLUE`)**: 372
- **Black with Blue Background (`Fore.BLACK`, `Back.BLUE`)**: 375, 376
- **Black with Cyan Background (`Fore.BLACK`, `Back.CYAN`)**: 366

</details>
