import discord
from discord.ext import commands
from api import *
from api.models import SheetWatcher

KUTILS_ICON = "https://media.allure.com/photos/5b7b0983b60c70133b1eaaf0/4:3/w_668,h_501,c_limit/Red%20Velvet%20Power%20Up.jpg"


# Kutils Cog
class Kutils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, name, time):
        ret = add_sheet_watcher(ctx.guild.id, name, time)
        if not issubclass(type(ret), Exception):
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
        if not jobs:
            await ctx.send("No jobs currently active.")
        else:
            embed = discord.Embed(title="Active Jobs", color=discord.Color.blue())
            embed.set_author(name='Kutils', icon_url=KUTILS_ICON)
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