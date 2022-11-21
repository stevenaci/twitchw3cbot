import twitchio
from twitchio.ext import commands, pubsub
from cogs.movies import MoviesCog
from cogs.warcraft import WarcraftCog
from tools.config import config

class TwitchBot(commands.Bot, twitchio.Client):


    def __init__(self):

        super().__init__(
            token= config['tokens']['access_token'],
            prefix='?',
            initial_channels=[c[0] for c in config['w3c']['channels']]
        )
        self.add_cog(WarcraftCog())
        #self.add_cog(MoviesCog(self))

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in - Ready')

    async def event_join(self, *args):
        print(f"Joined server{args}")

bot = TwitchBot()
bot.run()
