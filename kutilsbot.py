import os
import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = '.kutils ', case_insensitive = True)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Kutils'))
    print('Kutils is up and running.')

@client.command()
async def ping(ctx):
    await ctx.send(f'latency: {round(client.latency * 1000)}ms');

@client.command(aliases=['?'])
async def info(ctx):
    await ctx.send("This is the Kutils help page.")


client.run(os.getenv('TOKEN'))
