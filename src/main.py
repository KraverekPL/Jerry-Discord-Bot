import sys
import discord
import logging

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


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command(name='cytat')
async def cytat(ctx):
    singleQuote = random_quote_generator()
    await ctx.send(singleQuote)


@bot.command(name='tree')
async def generate_tree_img(ctx):
    image_url = random_tree_generator_url(url_tree_repo, class_parameter_value)
    logging.info(f"Generated url of tree: {image_url}")
    embed = discord.Embed(title="Random tree")
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
