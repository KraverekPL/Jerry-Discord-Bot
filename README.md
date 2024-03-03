# Discord Bot Readme

## Project Overview
This project is a Discord bot written in Python using the Discord.py library. The bot is designed to respond to specific keywords in messages, execute commands prefixed with '!', and perform various tasks such as clearing messages, generating random quotes, and displaying tree images.

## Setup and Configuration
### Requirements
- Python 3.6+
- Discord.py library
- Other dependencies specified in `requirements.txt`

### Configuration
The bot's token, log level, and other configuration parameters are stored in `config/configParserTool.py`. Ensure these values are appropriately set before running the bot.

### Keyword Responses
Keywords and corresponding responses are loaded from the `resources/keywords_responses.txt` file. Each line in the file should contain a keyword and its associated response separated by a colon.

## Usage

### Commands
1. **Ping:**
   - `!ping`: Tests the bot's responsiveness.

2. **Clear Messages:**
   - `!clear <amount>`: Clears messages in the channel based on the provided argument.
     - Use 'm' for minutes (e.g., `!clear 5m`).
     - Use a number for the last N messages (e.g., `!clear 10`).

3. **Random Quote:**
   - `!cytat`: Generates and sends a random quote.

4. **Tree Image:**
   - `!tree`: Generates and sends an embedded image of a tree.

5. **Fibonacci Sequence:**
   - `!fib <limit>`: Calculates and sends the Fibonacci sequence up to the specified limit.

### Events
- **on_ready:**
  - Event handler called when the bot is ready. Displays the bot's name and ID upon successful login.

- **on_message:**
  - Event handler called when a message is received. The bot responds to predefined keywords with a certain probability.

## Logging
The bot utilizes logging to provide information about its activities. Logs are displayed with timestamps, log levels, function names, and messages.

## Miscellaneous
The project includes utility functions for tasks such as generating random quotes, Fibonacci sequences, and tree images.

## Dependencies
- Discord.py
- Other dependencies specified in `requirements.txt`

## License
This project is open source and available under a non-commercial license. You are free to use and modify the code for non-commercial purposes. For details, please refer to the [LICENSE](LICENSE) file.

## Running the Bot
Execute the script to run the bot: `python bot_script.py`

## Note
Ensure that the necessary permissions are granted for the bot to perform actions like clearing messages.

Feel free to customize and extend the functionality as needed!
