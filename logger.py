import logging
from logging.handlers import RotatingFileHandler


class BotLogger:
    def __init__(self, log_file):
        self.logger = logging.getLogger("bot_logger")
        self.log_handler = RotatingFileHandler('bot.log', maxBytes=24, backupCount=5)
        self.log_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_handler = logging.FileHandler(log_file)
        log_handler.setFormatter(formatter)

        self.logger.addHandler(log_handler)

    def log(self, level, message):
        if level == 'info':
            self.logger.info(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'debug':
            self.logger.debug(message)

    def log_info(self, message):
        self.log('info', message)

    def log_error(self, message):
        self.log('error', message)

    def log_debug(self, message):
        self.log('debug', message)





