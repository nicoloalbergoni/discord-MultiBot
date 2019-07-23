from discord.ext import commands
import logging

logger = logging.getLogger(__name__)


class MultiBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)

    async def on_ready(self):
        logger.info(f'Logged in as {self.user.name}')

    async def on_command_error(self, ctx, exception):
        #await ctx.send(exception)
        logger.error(f'{ctx.command} raised an exception: {exception}')


