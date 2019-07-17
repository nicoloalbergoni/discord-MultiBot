from discord.ext import commands
from secret import BOT_TOKEN
from Music import Music

import logging

logger = logging.getLogger(__name__)

bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name}')


@bot.command()
async def test(ctx, url: str, time: str = None):
    logger.info(
        f'User {ctx.author.name} called the {ctx.command.name} command')
    # channel = ctx.author.voice.channel
    # vc = await channel.connect()


def main():
    logging.getLogger('discord').setLevel(logging.WARNING)
    logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        level=logging.INFO)

    bot.add_cog(Music(bot))
    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
