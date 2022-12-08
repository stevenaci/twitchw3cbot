import requests as re
from tools.singleton import Singleton
from apis.w3c.interface import Match, PlayerStats

base_url= "https://statistic-service.w3champions.com/api"

class W3CApi():
    realm_map = {10:'America', }

    race_map = {
        1:"Hu",
        2:"Or",
        8:"Ud",
        4:"Ne",
        0:"Rd"
    }
    def get(route: str):
        try:
            res = re.get(base_url + route)
            res = res.json()
            return res
        except:
            return None

    def get_player_stats(player_url: str):
        endpoint = "/players/"
        return PlayerStats(**W3CApi.get(endpoint + player_url))

    def get_current_match(player_url: str):
        endpoint = "matches/ongoing/"
        return  Match(**W3CApi.get(endpoint + player_url))


if __name__ == '__main__':
    # base class type singleton
    class TestClass_1(W3CApi):
        pass

    import unittest

    class TestStringMethods(unittest.TestCase):
        def test_singleton(self):
            c1_1 = TestClass_1.instance()
            print(c1_1.get_player_stats("blue%23%17562"))

    unittest.main()

