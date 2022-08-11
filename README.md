# Insult bot
A Discord bot that insults server users using a line from a text file
By default there is a 1% chance a user will be insulted with a random insult after posting a message

# Requirements
- Python 3
- [Discord Python library](https://pypi.org/project/discord.py/)
- [dotenv Python library](https://pypi.org/project/dotenv/)
- Discord API token (follow the guide linked in the Installation section)

# Installation

I have mostly followed [this guide](https://python.plainenglish.io/hello-world-how-to-make-a-simple-discord-bot-using-discord-py-c532611681ba) for the basics

1. Get the code
2. Create .env file in the same location as insultbot.py
3. Place inside the file: ```BOT_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'```
4. Run the code

<span style=color:Red>IMPORTANT:</span> Your bot works as long as the code is running. You may consider setting up a service. I've tested the code on Windows but set it up on Raspberry Pi (hence the occasional system check)

# Available commands

## Admin only

1. **!reload_insults** - when you change the content of the insults.txt you can run it to include new insults. No need to restart the bot

## Users

1. **!info** - provides basic info: number of insults, percentage chance, user commands
2. **!insult_me** - insults the user instantly
3. **!chance X** - changes the chance for an iunsult to X %
4. **!killbot** - this shuts down the bot from the Discord level in case you do not have access to your computer and things get out of hand