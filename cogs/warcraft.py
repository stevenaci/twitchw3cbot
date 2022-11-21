from tools.apis.w3c.player import Player, Players
from twitchio.ext import commands

from tools.config import config

class WarcraftCog(commands.Cog):

    players: dict[str, Player]

    def __init__(self):
        self.players = {}
        for chan, btag in config['w3c']['channels']:
            self.players[chan] = Player(btag)

    @commands.command()
    async def game(self, ctx: commands.Context):
        # look up stats based on channel
        if self.players.get(self.players[ctx.channel.name]):
            await ctx.channel.send(self.players[ctx.channel.name].get_current_match())

    @commands.command()
    async def join(self, ctx: commands.Context):
        if ctx.channel.name == 2:
            player = Player(ctx.message.content.split("#")[0:2]) # to do split # and name
            stats = Player.get_stats()
            if player.get_stats(): # check if they used a valid battle tag
                self.players[ctx.message.author] = player
                ctx.channel.send(f"That's {stats.battleTag()} ?")
            else:
                ctx.channel.send("Couldn't find that player on w3c")

    @commands.command()
    async def status(self, ctx: commands.Context):
        await ctx.channel.send(f"{self.players[ctx.channel.name]}")