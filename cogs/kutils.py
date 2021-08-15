import discord
from discord.ext import commands
from api import *

# Kutils Cog
class Kutils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, name):
        await ctx.send("add")
        add_sheet_watcher(ctx.guild.id, name)

    @commands.command()
    async def remove(self, ctx, name):
        await ctx.send("remove")

    @commands.command()
    async def show(self, ctx):
        await ctx.send("show")
        for name in get_sheet_watchers(ctx.guild.id):
            print(name)

    @commands.command()
    async def check(self, ctx):
        await ctx.send("check")


def setup(client):
    client.add_cog(Kutils(client))
    print("Kutils cog initializing...")