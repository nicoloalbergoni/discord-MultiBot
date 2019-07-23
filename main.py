from secret import BOT_TOKEN
from Music import Music
from bot import MultiBot

import logging

logger = logging.getLogger(__name__)


def main():
    logging.getLogger('discord').setLevel(logging.WARNING)
    logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        level=logging.INFO)

    bot = MultiBot(command_prefix='?')
    bot.add_cog(Music(bot))
    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
