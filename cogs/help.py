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
            'aliases': ['h']
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

    @commands.Cog.listener()
    async def on_message(self, message):
        if (self.client.user.mentioned_in(message) and message.content.find(" ") < 0) or message.content == '.kutils':
            msg = "To get started, type '.kutils help'."
            embed = discord.Embed(title="", description=msg, color=KUTILS_COLOR_THEME)
            await message.channel.send(embed=embed)

    @commands.command(aliases=["about"])
    async def info(self, ctx):
        title = "About Kutils"
        desc = "A service that automates checks for dead YouTube links on Google spreadsheets."
        embed = discord.Embed(title=title, description=desc, color=KUTILS_COLOR_THEME)
        embed.add_field(name="Bot Tag", value=self.client.user)
        embed.add_field(name="Version", value="1.0")
        embed.add_field(name="Authors", value="mecha#7999 & Brandon#0717", inline=False)
        embed.set_footer(text="Type '.kutils help' to get started.")
        await ctx.send(embed=embed)


# TODO implement custom help command
class CustomHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s %s' % (command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        title = "Kutils Help"
        embed = discord.Embed(title=title, color=KUTILS_COLOR_THEME)

        for cog, command in mapping.items():
            print(command)
            _filtered = []
            for c in command:
                _filtered.append(c)
                if isinstance(c, commands.Group):
                    [_filtered.append(subc) for subc in c.commands]

            filtered = await self.filter_commands(_filtered, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, 'qualified_name', 'Other')
                embed.add_field(name=cog_name, value='\n'.join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)

    async def send_group_help(self, group):
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command))
        embed.add_field(name='Command Help:', value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name='Aliases', value=', '.join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_error_message(self, error):
        embed = discord.Embed(title='Help command error!', description=error, color=KUTILS_COLOR_THEME)
        channel = self.get_destination()
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
    print("Help cog initializing...")
