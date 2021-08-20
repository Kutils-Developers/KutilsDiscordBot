import os
import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

cogs = ['kutils', 'help', 'misc']

client = commands.Bot(command_prefix=commands.when_mentioned_or('.kutils '), case_insensitive=True)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Kutils'))
    print('Kutils is up and running.')

for cog in cogs:
    client.load_extension(f'cogs.{cog}')
    
client.run(os.getenv('DISC_TOKEN'))
