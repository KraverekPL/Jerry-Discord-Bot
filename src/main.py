import datetime
import discord
import logging
import os

from discord.ext import commands
from config.configParserTool import bot_token, log_level, url_tree_repo, class_parameter_value
from functions.functions import *

# Logging configuration
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s  - %(funcName)s - %(message)s')

# Obtain current path and current directory
current_path = os.path.abspath(__file__)
current_directory = os.path.dirname(os.path.abspath(__file__))
logging.info(f"__file__ is: {current_path}")

# Load keywords and responses from file
file_path = os.path.join(current_directory, 'resources', 'keywords_responses.txt')
with open(file_path, 'r') as file:
    keyword_responses = [line.strip().split(':') for line in file]

# Discord.py bt configuration
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    """Event handler called when the bot is ready."""
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.event
async def on_message(message):
    """Event handler called when a message is received."""
    if message.author.bot:
        return
    for keyword, response in keyword_responses:
        if keyword.lower() in message.content.lower():
            if random.random() < 0.2:
                logging.info(f"Keyword response on_message: {keyword.lower()}:{response}")
                await message.channel.send(response)
            else:
                logging.info(f"No response - random.random() decided :)")
    await bot.process_commands(message)


@bot.command(name='ping')
async def ping(ctx):
    """Ping command to test bot's responsiveness."""
    await ctx.send('Pong!')


@bot.command(name='clear')
async def clear_messages(ctx, amount: str):
    """Clears messages in the channel based on the provided argument."""
    if ctx.author.guild_permissions.manage_messages:
        if 'm' in amount:
            current_time = datetime.datetime.utcnow()
            minutes = int(amount.rstrip('m'))
            past_time = current_time - datetime.timedelta(minutes=minutes)
            await ctx.channel.purge(before=current_time, after=past_time)
            logging.info(f'Messages from the last {minutes} minutes have been deleted')
        else:
            try:
                number_of_messages = int(amount)
                await ctx.channel.purge(limit=number_of_messages + 1)
                logging.info(f'The last {number_of_messages + 1} messages have been cleared')
            except ValueError:
                logging.info(f'Error while parsing to int')

    else:
        await ctx.send('You are not authorized!')


@bot.command(name='cytat')
async def cytat(ctx):
    """Generates and sends a random quote."""
    singleQuote = random_quote_generator()
    await ctx.send(singleQuote)


@bot.command(name='tree')
async def generate_tree_img(ctx):
    """Generates and sends an embedded image of a tree."""
    image_url = random_tree_generator_url(url_tree_repo, class_parameter_value)
    logging.info(f"Generated url of tree: {image_url}")
    embed = discord.Embed(title="Wonderful nature", colour=discord.Colour(0x00FF00))
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)


@bot.command(name='fib')
async def fib(ctx, arg: str = None):
    """Calculates and sends the Fibonacci sequence up to the specified limit."""
    if arg is None:
        await ctx.send('Please add one argument, like !fib 100')
        logging.info('Please add one argument, like !fib 100')
        return

    try:
        arg = int(arg)
    except ValueError:
        await ctx.send('Please send numeric value')
        logging.info('Not an integer value found in arg.')
        return

    if arg < 100000:
        result = fibonacci_sequence(arg)
        await ctx.send(f'{result}')
        logging.info(f'Invoking fibonacci seq method for n={arg}')
    else:
        await ctx.send('Number is too big!')
        logging.info('Number is too big!')


bot.run(bot_token)
