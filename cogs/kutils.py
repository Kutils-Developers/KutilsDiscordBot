import discord
from discord.ext import commands
from api import *
from api.models import SheetWatcher


# Kutils Cog
class Kutils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, name, time):
        await ctx.send(f'adding {name}...')
        add_sheet_watcher(ctx.guild.id, name, time)

    @commands.command()
    async def remove(self, ctx, name):
        await ctx.send(f'removing {name}...')
        try:
            pop_sheet_watcher(ctx.guild.id, name)
        except Exception as e:
            await ctx.send("hi")

    @commands.command()
    async def show(self, ctx):
        await ctx.send("showing jobs...")
        jobs = get_sheet_watchers(ctx.guild.id)
        for j in jobs:
            await ctx.send(j)

    @commands.command()
    async def check(self, ctx):
        await ctx.send("check")


def setup(client):
    client.add_cog(Kutils(client))
    print("Kutils cog initializing...")