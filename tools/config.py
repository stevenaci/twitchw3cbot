
from configparser import ConfigParser
from tools.singleton import Singleton


class Config(ConfigParser, Singleton):
    def __init__(self):
        super().__init__()
        self.read('twitch.ini')

config = Config()