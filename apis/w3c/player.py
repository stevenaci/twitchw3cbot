from enum import Enum
from apis.w3c.api import W3CApi
from apis.w3c.interface import Match, MatchPlayer, PlayerStats
from cogs.helpers import send_message
from tools.config import Config

from twitchio.ext import commands

class Players(dict):

    def __init__(self, **config):
        self.load_players()

    async def add_player(self, ctx: commands.Context, fullname: str):
        player = Player(ctx.message.author, fullname)
        stats = player.get_stats()
            # check if battle tag is valid
        if stats:
            self[ctx.message.author] = player
            await send_message(ctx, f"{stats.battleTag} was assigned to channel {ctx.message.author}")
        else:
            cnt_find = "Couldn't find that player on w3c."
            await send_message(ctx, f"reall y its.. {fullname} ? {cnt_find}" )

    async def find_player_match(self, ctx: commands.Context):
        if self.players.get(self.players[ctx.channel.name]):
            await send_message(ctx, self.players[ctx.channel.name].get_current_match())

    def load_players(self):

        with open('players.save', 'r') as f:            
            for p in f.readlines():
                twitch_channel, bnet_id = p.split(":")
                self[twitch_channel] = Player(twitch_channel, bnet_id)

    def save(self):
        with open('players.save', 'wb') as f:
            for k, v in self.items():
                f.write(f"{k}:{v}")


class Player():

    name: str

    def __init__(self, channel, full_name: str):
        
        self.channel = channel
        self.name, self.id = full_name.split("#")[0:2]
        assert self.name and self.id
        print(self.get_stats())
        return

    @property
    def url_route(self)-> str:
        return f"{self.name}%23{self.id}"

    def get_current_match(self) -> Match:
        try:
            return W3CApi.get_current_match(self.url_route)
        except:
            return None

    def get_stats(self) -> PlayerStats:
        try:
            return W3CApi.get_player_stats(self.url_route)
        except:
            return None

#player = Player("ToD", 2792)
#player = Player("iNSUPERABLE", 11842)