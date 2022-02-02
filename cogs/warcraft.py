from twitchio.ext import commands

class WarcraftCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.event()
    async def event_message(self, message):
        # An event inside a cog!
        if message.echo:
            return

        print(message.content)
    @commands.command()
    async def whatever(self, ctx):
        channel = self.bot.get_channel(8675309) #whatever your channel id is
        await channel.send("whatever")

def prepare(bot: commands.Bot):
    # Load our cog with this module...
    bot.add_cog(WarcraftCog(bot))