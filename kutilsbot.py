import os
import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

client.run(os.getenv('TOKEN'))
