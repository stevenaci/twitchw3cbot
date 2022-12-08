from enum import Enum
import pickle
from apis.w3c.api import W3CApi
from apis.w3c.interface import Match, MatchPlayer, PlayerStats
from tools.config import Config

class Players(dict):

    def __init__(self, **config):
        self.load_players()

    def load_players(self):

        with open('players.pickle', 'r') as f:            
            if f.read(1):
                try:
                    self = pickle.load(f)
                finally:
                    pass

    def save(self):
        with open('players.pickle', 'wb') as f:
            try:
                pickle.dump(self, f)
            finally:
                pass


class Player():

    name: str

    def __init__(self, channel, name: str, bnet_id: int):
        self.channel = channel
        self.name = name
        self.id = bnet_id
        print(self.get_stats())
        return

    def save(self):
        with open(self.name,'wb') as f:
            pickle.dump(self, f)
        pass

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

players = Players()
#player = Player("ToD", 2792)
#player = Player("iNSUPERABLE", 11842)