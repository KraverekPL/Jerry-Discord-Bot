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
async def fib(ctx, arg: int = None):
    logging.info('Invoking fibonacci seq method')
    if arg is not None:
        if arg < 100000:
            result = fibonacci_sequence(arg)
            await ctx.send(f'{result}')
            logging.info(f'Invoking fibonacci seq method for n={arg}')
        else:
            await ctx.send('Number is too big!')
            logging.info('Number is too big!')
    else:
        await ctx.send('Please add one argument, like !fib 100')
        logging.info('Please add one argument, like !fib 100')


bot.run(botToken)
