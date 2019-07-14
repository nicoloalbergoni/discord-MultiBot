import logging

# Define MESSAGE log level
MESSAGE = 25
# "Register" new loggin level
logging.addLevelName(MESSAGE, 'MESSAGE')


class Logger(logging.Logger):
    def message(self, msg, *args, **kwargs):
        if self.isEnabledFor(MESSAGE):
            self._log(MESSAGE, msg, args, **kwargs)