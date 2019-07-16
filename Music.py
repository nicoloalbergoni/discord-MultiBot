from discord.ext import commands
from YTDLSource import YTDLSource

import logging

logger = logging.getLogger(__name__)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dc')
    async def disconnect(self, ctx):
        """Stops and disconnects the bot from voice"""
        logger.info(f'Disconnected from voice channel: {ctx.voice_client.channel.name}')
        await ctx.voice_client.disconnect()

    @commands.command(name='p')
    async def play(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(
                'Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(player.title))

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client is None or not ctx.voice_client.is_playing():
            await ctx.send('No song is currently playing')
        else:
            # TODO: fixare title attribute not found
            ctx.voice_client.stop()
            logger.info(f'{ctx.author.name} skipped song {ctx.voice_client.source.title}')
            await ctx.send(f'Skipped song: {ctx.voice_client.source.title}')

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError(
                    "Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
