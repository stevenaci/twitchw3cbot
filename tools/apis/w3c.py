import requests as re

class W3CApi():
    base_url= "https://statistic-service.w3champions.com/api/"
    
    realm_map = {
        10:'America',
    }

    race_map = {
        1:"Hu",
        2:"Or",
        8:"Ud",
        4:"Ne",
        0:"Rd"
    }
    def get_json(url: str):
        res = re.get(W3CApi.base_url + url)
        try:
            res = res.json()
            return res
        except:
            return None


class Player():

    def __init__(self, name, id):
        self.name = name
        self.id = str(id)
        self.url_name = self.name + "%23" + self.id
        return

    def get_current_match(self):
        endpoint = "matches/ongoing/"
        return W3CApi.get_json(endpoint + self.url_name)

    def get_stats(self):
        endpoint = "players/"
        return W3CApi.get_json(
            endpoint + self.url_name) # idk

player = Player("ToD", 2792)

"""
{'map': 'amazonia', 'id': '5f40632b4521d79a2975cd8d', 'durationInSeconds': 0,
'startTime': '2020-08-22T00:13:04.235+00:00', 'endTime': '0001-01-01T00:00:00+00:00',
'gameMode': 1, 'teams': [{'players': [{'race': 4, 'oldMmr': 2066, 'currentMmr': 0,
'battleTag': 'walterelfo#1110', 'name': 'walterelfo', 'mmrGain': -2066, 'won': False,
'location': 'CL', 'country': None}], 'won': False},
{'players': [{'race': 1, 'oldMmr': 2095, 'currentMmr': 0, 'battleTag': 'Fish#14989', 'name': 'Fish', 'mmrGain': -2095, 'won': False, 'location': 'SG', 'country': 'Kuwait'}], 'won': False}],
'gateWay': 10, 'season': 0}
https://statistic-service.w3champions.com/api/players/Minigun%2311620/winrate?season=2
"""
data = player.get_cur_match()
if data:
    i = 0
    for team in data["teams"]:
        i+=1
        print("TEAM 1" if i == 1 else "TEAM 2")
        for player in team["players"]:
            #print(player)
            print(player["name"], race_map[player["race"]], player['oldMmr'])


def get_elapsed(start_timestamp):

    return

