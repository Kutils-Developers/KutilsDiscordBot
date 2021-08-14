from discord.ext import commands

# Misc Cog
class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(ctx.guild.id)
        await ctx.send(f'pong {round(self.client.latency * 1000)}ms')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # add guild to mongo
        print(guild.id)


def setup(client):
    client.add_cog(Misc(client))
    print("Misc cog initializing...")