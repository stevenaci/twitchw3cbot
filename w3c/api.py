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

