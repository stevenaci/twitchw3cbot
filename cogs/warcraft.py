from tools.config import Config
from twitchio.ext import commands
from apis.w3c.player import Player, players

class WarcraftCog(commands.Cog):

    def __init__(self, bot: commands.Bot, server_channel: str):
        self.channel_name = server_channel
        self.bot = bot
        pass

    @commands.command()
    async def find_player_game(self, ctx: commands.Context):
        # look up stats based on channel
        if self.players.get(self.players[ctx.channel.name]):
            await ctx.channel.send(self.players[ctx.channel.name].get_current_match())

    @commands.command()
    async def join(self, ctx: commands.Context):

        if ctx.channel.name == self.channel_name: # my channel
            name, id = ctx.message.content.split(" ")[1].split("#")[0:2]
            player = Player(ctx.message.author, name, id)
            stats = player.get_stats()
            if stats: # check if they used a valid battle tag
                # Add player to the pool
                players[ctx.message.author] = player
                await ctx.channel.send(f"{stats.battleTag} was registered on {ctx.message.author}")
            else:
                cnt_find = "Couldn't find that player on w3c"
                await ctx.channel.send(
                    f"reall y its.. {name}#{id} ? {cnt_find}" )

    @commands.command()
    async def leave(self, ctx: commands.Context):
        if ctx.channel.name == 2: # my channel
            del players[ctx.message.author]

    @commands.command()
    async def player_status(self, ctx: commands.Context):
        await ctx.channel.send(f"{players[ctx.channel.name]}")