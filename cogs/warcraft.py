from twitchio.ext import commands
from w3c.players import Players

class WarcraftCog(commands.Cog):

    server_channel: str
    players: Players

    def __init__(self, players: Players, bot: commands.bot):
        self.players = players
        self.bot = bot
    
    def set_server_channel(self, channel: str):
        print(f"Setting Clockwerk Server as channel: {channel}")
        self.server_channel =  channel

    def is_server_channel(self, ctx: commands.Context):
        return ctx.channel.name == self.server_channel

    @commands.command()
    async def oppo(self, ctx: commands.Context):
        """ Returns: Info for the player's current match"""
        await self.players.find_player_match(ctx)

    @commands.command()
    async def join(self, ctx: commands.Context):
        """ Command to join the Clockwerk Network, 
            or to change the player associated with your account.
            If the message is sent
        """
        if self.is_server_channel(ctx) or ctx.message.author.is_broadcaster:
            try:
                battletag = ctx.message.content.split(" ")[1]
            except:
                await ctx.channel.send("Specify A BattleTag :OVVVO:!")
                return
            try:
                await self.players.add_player(ctx.message.author.name, battletag)
                await ctx.channel.send(f"Battletag {battletag} was assigned to channel {ctx.message.author.name}")
                if self.players.get(ctx.message.author.name):
                    await self.bot.join_channels([ctx.message.author.name])
            except:
                await ctx.channel.send("Couldn't find that battletag on w3c network.")

    @commands.command()
    async def leave(self, ctx: commands.Context):
        if self.is_server_channel(ctx) or ctx.message.author.is_broadcaster:
            if self.players.remove_player(ctx.author.name):
                await ctx.channel.send(f" {ctx.author.name}, your channel has been removed!")
                self.bot.part_channels([ctx.author.name])
            else:
                await ctx.channel.send(f"No player currently assigned to the channel: {ctx.author.name}")

    @commands.command()
    async def player_status(self, ctx: commands.Context):
        await ctx.channel.send(f"{self.players[ctx.channel.name]}")
