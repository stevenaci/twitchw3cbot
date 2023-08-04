import twitchio
from twitchio.ext import commands
from cogs.warcraft import WarcraftCog
from tools.config import config
from w3c.players import players

class TwitchBot(commands.Bot, twitchio.Client):


    def __init__(self):
        super().__init__(
            prefix='?',
            token=config['creds']['access_token']
        )
        self.add_cog(WarcraftCog(bot=self))
        self.run()

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in - Ready')
        await self.join_channels(
            [*players.keys(), self.nick]
        )

    async def event_join(self, *args):
        print(f"Joined server{args}")

if __name__ == '__main__':
    bot = TwitchBot()
    bot.run()
