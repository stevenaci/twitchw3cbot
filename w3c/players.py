from twitchio.ext import commands
from tools.environment import environment
from w3c.player import Player
from w3c.w3c_interface import Match

class Players(dict):
    def __init__(self, testing = True, **config):
        self.load_players()

    async def add_player(self, twitch_name, battletag: str):
        player = Player(twitch_name, battletag)
        stats = player.get_stats()
        assert stats
        self[twitch_name] = player
        self.save()

    def remove_player(self, twitch_name):
        if self.get(twitch_name):
            del self[twitch_name]
            self.save()
            return True
        return False

    async def find_player_match(self, channel_name) -> tuple[Match, Player]:
        if self.get(channel_name):
            player: Player = self[channel_name]
            return player.get_current_match(), player
        else: raise Exception("No player found.")


    def load_players(self):
        if environment.isTesting:
            return
        with open("players.save", "r") as f:
            for p in f.readlines():
                twitch_channel, bnet_id = p.split(":")
                self[twitch_channel] = Player(twitch_channel, bnet_id)

    def save(self):
        if environment.isTesting:
            return
        with open("players.save", "w") as f:
            f.writelines([f"{k}:{v.bnet}" for k, v in self.items()])
