import discord
from discord.ext import commands
from api import *
from api.models import SheetWatcher

KUTILS_COLOR_THEME = discord.Color.blue()


# Kutils Cog
class Kutils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, name, time):
        ret = add_sheet_watcher(ctx.guild.id, name, time)
        if not isinstance(ret, Exception):
            await ctx.send(f'Added {name}!')
        else:
            await ctx.send(f'API ERROR: {str(ret)}')

    @commands.command(aliases=["delete"])
    async def remove(self, ctx, name):
        if pop_sheet_watcher(ctx.guild.id, name):
            await ctx.send(f'Removed {name}!')
        else:
            await ctx.send("No job with matching name.")

    @commands.command()
    async def show(self, ctx):
        jobs = get_sheet_watchers(ctx.guild.id)
        print("got jobs")
        print(jobs)
        if not jobs:
            print("jobs empty")
            embed = discord.Embed(title="No active jobs.", color=KUTILS_COLOR_THEME)
            embed.set_footer(text="To add a job, use .kutils add")
        else:
            print("jobs not empty")
            embed = discord.Embed(title="Active Jobs", color=KUTILS_COLOR_THEME)
            # embed.set_author(name='Active Jobs', icon_url=KUTILS_ICON)
            for job in jobs:
                embed.add_field(name=job.name, value=job.utc_offset)
            embed.set_footer(text="To add or remove jobs, use .kutils add/remove")
        await ctx.send(embed=embed)

    @commands.command()
    async def check(self, ctx):
        await ctx.send("check")


def setup(client):
    client.add_cog(Kutils(client))
    print("Kutils cog initializing...")