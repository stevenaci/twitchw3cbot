import requests as re
from w3c.interface import Match, PlayerStats

base_url= "https://statistic-service.w3champions.com/api/"

class W3CApi():

    def get_json(route: str):
        try:
            res = re.get(base_url + route)
            return res.json()
        except:
            return dict()

    def get_player_stats(player_url: str):
        endpoint = "players/"
        return PlayerStats(**W3CApi.get_json(endpoint + player_url))

    def get_current_match(player_url: str):
        endpoint = "matches/ongoing/"
        return  Match(**W3CApi.get_json(endpoint + player_url))
