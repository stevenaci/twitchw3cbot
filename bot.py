from twitchio.ext import commands as commands
from cogs.warcraft import WarcraftCog
import configparser

class myBot(commands.Bot):

    channels = ['protectionfromblue'] # Twitch channel to watch
    token = "oauth:thisisnotarealoathtoken" # Oauth2 token

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('twitch.ini')
        super().__init__(
            token= config['twitch']['access_token'],
            prefix='?',
            initial_channels= myBot.channels
        )
    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | moi')

bot = myBot()
bot.run()

def prepare(bot: commands.Bot):
    bot.add_cog(WarcraftCog(bot))



























class myBot(commands.Bot):

    def __init__(
        self, **kwargs):
        super().__init__(**kwargs)
bot = commands.Bot(
    {
            
    })

# Register an event with the bot
@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')

@bot.event
async def event_message(message):
    print(message.content)

    # If you override event_message you will need to handle_commands for commands to work.
    await bot.handle_commands(message)


bot.run()

def prepare(bot: commands.Bot):
    bot.add_cog(Warcraft(bot))