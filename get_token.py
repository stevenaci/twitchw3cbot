import requests as re
from tools.config import config

def get_token() -> str:
    res = re.post(
        url="https://id.twitch.tv/oauth2/token",
        data={
            "client_id":config['credential']['client_id'],
            "client_secret":config['credential']['client_secret'],
            "grant_type":"client_credentials"
        }
    )
    return res.json().get('access_token')
