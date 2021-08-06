import discord
from discord.ext import commands

class Kutils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'latency: {round(client.latency * 1000)}ms');
        await ctx.send(ctx.guild.id)


def setup(client):
    client.add_cog(Kutils(client))