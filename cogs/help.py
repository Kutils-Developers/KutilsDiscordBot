import discord
from discord.ext import commands

KUTILS_COLOR_THEME = discord.Color.blue()


# Help Cog
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        help_attributes = {
            'help': 'Displays help for Kutils commands',
            'hidden': True,
            'aliases': ['h', 'info']
        }
        help_obj = CustomHelp(command_attrs=help_attributes, verify_checks=False)
        client.help_command = help_obj

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            msg = "Invalid command."
            embed = discord.Embed(title=msg, color=KUTILS_COLOR_THEME)
            embed.set_footer(text="Type '.kutils help' for more info.")
            await ctx.send(embed=embed)


# TODO implement custom help command
class CustomHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        return await super().send_bot_help(mapping)

    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)

    async def send_group_help(self, group):
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        return await super().send_command_help(command)


def setup(client):
    client.add_cog(Help(client))
    print("Help cog initializing...")