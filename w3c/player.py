from w3c.w3c_service import W3CApi
from w3c.w3c_interface import Match, PlayerStats
import traceback

class Player():

    name: str

    def __init__(self, bnet: str):
        self.bnet = bnet
        self.name, self.id = [s for s in bnet.split("#")[0:2]]
        assert self.name and self.id

    @property
    def url(self)-> str:
        return f"{self.name}%23{self.id}"

    def get_current_match(self) -> Match: return W3CApi().get_current_match(self.url)

    def get_stats(self) -> PlayerStats: return W3CApi().get_player_stats(self.url)


