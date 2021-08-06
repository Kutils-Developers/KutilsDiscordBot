import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['?'])
    async def info(self, ctx):
        await ctx.send("This is the Kutils help page.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command. Type '.kutils help' for more info.")

def setup(client):
    client.add_cog(Help(client))