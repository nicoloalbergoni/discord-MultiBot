from discord.ext import commands
from secret import BOT_TOKEN
import logging
from Music import Music

logging.basicConfig(level=logging.INFO,
                    format='%(process)d-%(levelname)s-%(message)s')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name}')


@bot.command()
async def test(ctx, url: str, time: str = None):
    logging.info(
        f'User {ctx.author.name} called the {ctx.command.name} command')
    # channel = ctx.author.voice.channel
    # vc = await channel.connect()


bot.add_cog(Music(bot))
bot.run(BOT_TOKEN)
