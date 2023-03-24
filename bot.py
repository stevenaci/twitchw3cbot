import twitchio
from twitchio.ext import commands, pubsub
from cogs.warcraft import WarcraftCog
from tools.config import Config

class TwitchBot(commands.Bot, twitchio.Client):


    def __init__(self):

        super().__init__(
            token= Config()['tokens']['access_token'],
            prefix='?',
            initial_channels=[Config()['w3c']['server_channel']]
        )
        self.add_cog(WarcraftCog(bot=self, server_channel=Config()['w3c']['server_channel']))
        self.run()

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in - Ready')

    async def event_join(self, *args):
        print(f"Joined server{args}")
        await self.connected_channels[0].send("online")
if __name__ == '__main__':
    bot = TwitchBot()
    bot.run()
