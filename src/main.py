import datetime
import sys
import discord
import logging
import os

from discord.ext import commands
from config.configParserTool import bot_token
from config.configParserTool import log_level
from config.configParserTool import url_tree_repo
from config.configParserTool import class_parameter_value

sys.path.append("../")
from functions.functions import *

logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)
current_path = os.path.abspath(__file__)
current_directory = os.path.dirname(os.path.abspath(__file__))
logging.info(f"__file__ is: {current_path}")

file_path = os.path.join(current_directory, 'resources', 'keywords_responses.txt')
with open(file_path, 'r') as file:
    keyword_responses = [line.strip().split(':') for line in file]


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.event
async def on_message(message):
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
    await ctx.send('Pong!')


@bot.command(name='clear')
async def clear_messages(ctx, amount: str):
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
    singleQuote = random_quote_generator()
    await ctx.send(singleQuote)


@bot.command(name='tree')
async def generate_tree_img(ctx):
    image_url = random_tree_generator_url(url_tree_repo, class_parameter_value)
    logging.info(f"Generated url of tree: {image_url}")
    embed = discord.Embed(title="Wonderful nature", colour=discord.Colour(0x00FF00))
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)


@bot.command(name='fib')
async def fib(ctx, arg: str = None):
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
