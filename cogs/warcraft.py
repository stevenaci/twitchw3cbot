from cogs.helpers import matches_channel, send_message
from twitchio.ext import commands
from w3c.players import players

class WarcraftCog(commands.Cog):

    def __init__(self, bot: commands.Bot):

        self.bot = bot
        pass

    def is_server_channel(self, ctx: commands.Context):
        return matches_channel(ctx, self.bot.nick)

    @commands.command()
    async def who(self, ctx: commands.Context):
        words = ctx.message.content.split(" ")
        if (words[1] == "is" and words[2] == "oppo"):
            await players.find_player_match(ctx)

    @commands.command()
    async def join(self, ctx: commands.Context):
        if self.is_server_channel(ctx) or ctx.message.author.is_broadcaster:
            fullname = ctx.message.content.split(" ")[1]
            stats = await players.add_player(
                ctx.message.author.name, fullname
            )
            if stats:
                await send_message(ctx, f"{stats.battleTag} was assigned to channel {ctx.message.author.name}")
            else:
                cnt_find = "Couldn't find that player on w3c."
                await send_message(ctx, cnt_find)


    @commands.command()
    async def leave(self, ctx: commands.Context):
        if self.is_server_channel(ctx) or ctx.message.author.is_broadcaster:
            if players.remove_player(ctx.author.name):
                await send_message(ctx, f"{ctx.author.name}, your channel has been removed!")
            else:
                await send_message(ctx, f"No player currently assigned to the channel: {ctx.author.name}")

    @commands.command()
    async def player_status(self, ctx: commands.Context):
        await ctx.channel.send(f"{players[ctx.channel.name]}")