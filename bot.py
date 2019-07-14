from discord.ext import commands
from bot_logger import Logger
from secret import BOT_TOKEN
import logging
from Music import Music

logging.basicConfig(level=logging.MESSAGE,
                  format='%(process)d-%(levelname)s-%(message)s')

logging.setLoggerClass(Logger)
logger = logging.getLogger('Bot Logger')
logger.message('This seems to work')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name}')


@bot.command()
async def test(ctx, url: str, time: str = None):
    logger.info(
        f'User {ctx.author.name} called the {ctx.command.name} command')
    # channel = ctx.author.voice.channel
    # vc = await channel.connect()


bot.add_cog(Music(bot))
bot.run(BOT_TOKEN)
