from enum import Enum
from tools.apis.w3c import W3CApi
from tools.apis.w3c.interface import Match, MatchPlayer, PlayerStats

class Players(Enum):
    iNSUPERABLE = 11842

class Player():

    name: str

    def __init__(self, name: str):
        self.name = name
        print(self.get_stats())
        return

    @property
    def url(self)-> str:
        return f"{self.name.replace('#','%23')}"

    def get_current_match(self) -> Match:
        try:
            return Match(**W3CApi.get_current_match(self.url))
        except:
            return None

    def get_stats(self) -> PlayerStats:
        try:
            return PlayerStats(**W3CApi.get_player_stats(self.url))
        except:
            return None

#player = Player("ToD", 2792)
#player = Player("iNSUPERABLE", 11842)