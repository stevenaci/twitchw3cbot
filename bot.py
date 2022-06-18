import twitchio
from twitchio.ext import commands, pubsub
from cogs.movies import MoviesCog
from cogs.warcraft import WarcraftCog
import configparser

class myBot(commands.Bot, twitchio.Client):


    def __init__(self):
        config = configparser.ConfigParser()
        config.read('twitch.ini')

        super().__init__(
            token= config['tokens']['access_token'],
            prefix='?',
            initial_channels=[config['config']['channels']]
        )
        self.add_cog(MoviesCog(self))

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in - Ready')

    async def event_join(self, *args):
        print(f"Joined server{args}")

bot = myBot()
bot.run()
