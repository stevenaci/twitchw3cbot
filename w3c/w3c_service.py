import requests as re
from tools.environment import environment
from w3c.w3c_interface import Match, PlayerStats
from w3c.mock_data import test_player_stats, test_match


class Endpoints:
    PLAYERS = "players/"
    MATCHES_ONGOING = "matches/ongoing/"


class W3CServer:

    live_prefix = "https://"
    base_url = "statistic-service.w3champions.com/api/"

    def __init__(self) -> None:
        pass

    def full_url(self, end_point: str):
        return self.live_prefix + self.base_url + end_point


class W3CApi:

    server = W3CServer()

    def get_json(self, endpoint: str, player: str):
        try:
            return re.get(self.server.full_url(endpoint + player)).json()
        except:
            return {}

    def get_player_stats(self, player_url: str):
        return PlayerStats(**(
            self.get_json(Endpoints.PLAYERS, player_url)
            if not environment.isTesting
            else test_player_stats
        ))

    def get_current_match(self, player_url: str):
        return Match(
            **(
                self.get_json(Endpoints.MATCHES_ONGOING, player_url)
                if not environment.isTesting
                else test_match
            )
        )
