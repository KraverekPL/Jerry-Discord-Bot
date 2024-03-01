import sys
import discord
import logging

from discord.ext import commands
from config.configParserTool import botToken
from config.configParserTool import logLevel

sys.path.append("../")
from functions.functions import *

logging.basicConfig(level=logLevel, format='%(asctime)s - %(levelname)s - %(message)s')

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name} ({bot.user.id})')


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command(name='fib')
async def fib(ctx, arg: str = None):
    if arg is None:
        await ctx.send('Please add one argument, like !fib 100')
        logging.debug('Please add one argument, like !fib 100')
        return

    try:
        arg = int(arg)
    except ValueError:
        await ctx.send('Please send numeric value')
        logging.debug('Not an integer value found in arg.')
        return

    if arg < 100000:
        result = fibonacci_sequence(arg)
        await ctx.send(f'{result}')
        logging.info(f'Invoking fibonacci seq method for n={arg}')
    else:
        await ctx.send('Number is too big!')
        logging.debug('Number is too big!')


bot.run(botToken)
