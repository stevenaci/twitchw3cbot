from w3c.api import W3CApi
from w3c.interface import Match, PlayerStats


class Player():

    name: str

    def __init__(self, channel, bnet: str):
        self.bnet = bnet
        self.channel = channel
        self.name, self.id = [s.lower() for s in bnet.split("#")[0:2]]
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

