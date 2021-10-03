import discord
from discord.ext import commands
from api import *

KUTILS_COLOR_THEME = discord.Color.blue()


# Kutils Cog
class Kutils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, name, sheet_link, cell_ranges, time):
        ret = add_sheet_watcher(ctx.guild.id, name, sheet_link, cell_ranges, time)
        if not isinstance(ret, Exception):
            msg = f'Added {name}!'
            await ctx.send(embed=discord.Embed(title=msg, color=KUTILS_COLOR_THEME))
        else:
            msg = f'API ERROR: {str(ret)}'
            await ctx.send(embed=discord.Embed(title=msg, color=KUTILS_COLOR_THEME))

    @commands.command(aliases=["delete"])
    async def remove(self, ctx, name):
        ret = pop_sheet_watcher(ctx.guild.id, name)
        if not isinstance(ret, Exception):
            msg = f'Removed {name}!'
            await ctx.send(embed=discord.Embed(title=msg, color=KUTILS_COLOR_THEME))
        else:
            msg = f'API ERROR: {str(ret)}'
            await ctx.send(embed=discord.Embed(title=msg, color=KUTILS_COLOR_THEME))

    @commands.command()
    async def show(self, ctx):
        jobs = get_sheet_watchers(ctx.guild.id)
        if not jobs:
            msg = "No active jobs."
            embed = discord.Embed(title=msg, color=KUTILS_COLOR_THEME)
            embed.set_footer(text="To add a job, use .kutils add")
        else:
            embed = discord.Embed(title="Active Jobs", color=KUTILS_COLOR_THEME)
            for job in jobs:
                embed.add_field(name=job.name, value=job.utc_offset)
            embed.set_footer(text="To add or remove jobs, use .kutils add/remove")
        await ctx.send(embed=embed)

    @commands.command()
    async def check(self, ctx):
        dead_cells = get_updates(ctx.guild.id)
        await ctx.send(dead_cells)

    @add.error
    async def add_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments):
            msg = "Invalid number of arguments."
            desc = ".kutils add [name] [time]"
            embed = discord.Embed(title=msg, description=desc ,color=KUTILS_COLOR_THEME)
            embed.set_footer(text="Type '.kutils help' for more info.")
            await ctx.send(embed=embed)

    @remove.error
    async def remove_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments):
            msg = "Invalid number of arguments."
            desc = ".kutils remove [name]"
            embed = discord.Embed(title=msg, description=desc, color=KUTILS_COLOR_THEME)
            embed.set_footer(text="Type '.kutils help' for more info.")
            await ctx.send(embed=embed)

    @show.error
    async def show_error(self, ctx, error):
        if isinstance(error, commands.TooManyArguments):
            msg = "Invalid number of arguments."
            desc = ".kutils show"
            embed = discord.Embed(title=msg, description=desc, color=KUTILS_COLOR_THEME)
            embed.set_footer(text="Type '.kutils help' for more info.")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Kutils(client))
    print("Kutils cog initializing...")