from discord.ext import commands
from api import *


# Misc Cog
class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong {round(self.client.latency * 1000)}ms')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if not instance_exists(guild.id):
            create_instance(guild.id)

    @commands.command()
    async def rejoin(self, ctx):
        await ctx.send("rejoining...")
        if not instance_exists(ctx.guild.id):
            create_instance(ctx.guild.id)


def setup(client):
    client.add_cog(Misc(client))
    print("Misc cog initializing...")
