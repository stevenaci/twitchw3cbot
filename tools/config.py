
from configparser import ConfigParser


class Config(ConfigParser):
    def __init__(self):        
        self.read('twitch.ini')
    