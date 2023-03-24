from cogs.helpers import matches_channel, send_message
from twitchio.ext import commands
from apis.w3c.player import Players

class WarcraftCog(commands.Cog):

    def __init__(self, bot: commands.Bot, server_channel: str):
        self.server_channel = server_channel
        self.bot = bot
        self.players = Players()
        pass


    @commands.command()
    async def find_player_game(self, ctx: commands.Context):
        await self.players.find_player_match(ctx)


    @commands.command()
    async def join(self, ctx: commands.Context):

        if matches_channel(ctx, self.server_channel):
            fullname = ctx.message.content.split(" ")[1]
            await self.players.add_player(ctx, fullname)

    @commands.command()
    async def leave(self, ctx: commands.Context):
        if matches_channel(ctx, self.server_channel):
            try:
                del self.players[ctx.message.author]
                await send_message(ctx, f"{ctx.author.channel}, your channel has been removed!")
            except:
                await send_message(ctx, f"No player currently assigned to the channel: {ctx.author.channel}")

    @commands.command()
    async def player_status(self, ctx: commands.Context):
        await ctx.channel.send(f"{self.players[ctx.channel.name]}")