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

    def get_player_stats(player_url: str):
        endpoint = "players/"
        return W3CApi.get_json(endpoint + player_url)

    def get_current_match(player_url: str):
        endpoint = "matches/ongoing/"
        return  W3CApi.get_json(endpoint + player_url)


def get_elapsed(start_timestamp):

    return

