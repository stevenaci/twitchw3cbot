from twitchio.ext import commands

def matches_channel(ctx: commands.Context, channel: str):
    return ctx.channel.name == channel

async def send_message(ctx: commands.Context, msg: str):
    return await ctx.channel.send(msg)
