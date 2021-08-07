import discord
from discord.ext import commands
# from api import kutilsapi

# Kutils Cog
class Kutils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(ctx.guild.id)
        await ctx.send(f'latency: {round(self.client.latency * 1000)}ms');

    @commands.command()
    async def add(self, ctx, name, sheet_link, cell_range, time):
        await ctx.send("add")

    @commands.command()
    async def remove(self, ctx, name):
        await ctx.send("remove")

    @commands.command()
    async def show(self, ctx):
        await ctx.send("show")

    @commands.command()
    async def check(self, ctx):
        await ctx.send("check")

def setup(client):
    client.add_cog(Kutils(client))
    print("Kutils cog initializing...")