# -*- coding: utf-8 -*-

import logging
import logging.handlers
import sys
import os

from ndict import ndict

from config import CONFIG


class LoggerProvider(list):
    def __init__(self, *args, **kwargs):
        super(LoggerProvider, self).__init__(*args, **kwargs)

    def get(self, name):
        assert name not in list(map(lambda _: _[0], self)), 'Repeat Define Logger Name "%s"' % name
        logger = logging.getLogger(name)
        self.append((name, logger))
        return logger


logger_provider = LoggerProvider()

root_logger = logger_provider.get('root')
root_logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter(CONFIG.LOGGER.FORMAT))
stream_handler.setLevel(CONFIG.LOGGER.LEVEL)

root_file_handler = logging.handlers.TimedRotatingFileHandler(
    filename=os.path.join(CONFIG.LOGGER.OUTPUT_DIR, 'root.log'), when='midnight', interval=1,
    backupCount=7, encoding='utf-8'
)
root_file_handler.setFormatter(logging.Formatter(CONFIG.LOGGER.FORMAT))
root_file_handler.setLevel(logging.DEBUG)

root_logger.addHandler(stream_handler)
root_logger.addHandler(root_file_handler)

error_logger = logger_provider.get('root.error')
error_logger.setLevel(logging.ERROR)

error_file_handler = logging.handlers.TimedRotatingFileHandler(
    filename=os.path.join(CONFIG.LOGGER.OUTPUT_DIR, 'root.error.log'), when='midnight', interval=1,
    backupCount=7, encoding='utf-8'
)
error_file_handler.setFormatter(logging.Formatter(CONFIG.LOGGER.FORMAT))
error_file_handler.setLevel(logging.ERROR)

error_logger.addHandler(error_file_handler)


def _create_root_successor_logger(name):
    logger = logger_provider.get('root.' + name)

    time_rotating_file_handler = logging.handlers.TimedRotatingFileHandler(
        filename=os.path.join(CONFIG.LOGGER.OUTPUT_DIR, 'root.' + name + '.log'), when='midnight', interval=1,
        backupCount=7, encoding='utf-8'
    )
    time_rotating_file_handler.setFormatter(logging.Formatter(CONFIG.LOGGER.FORMAT))
    time_rotating_file_handler.setLevel(logging.DEBUG)

    logger.addHandler(time_rotating_file_handler)
    return logger


def _echo_init_info():
    def echo_config(dict, prefix='CONFIG'):
        for item in dict.items():
            if isinstance(item[1], type(ndict())):
                echo_config(item[1], prefix + '.' + item[0])
            else:
                root_logger.debug('%s.%s: %s' % (prefix, item[0], item[1]))

    root_logger.info('Config Choose: %s' % CONFIG.NAME)
    echo_config(CONFIG)
    root_logger.info('Loggers: %s' % [i[0] for i in logger_provider])

# DEFINE YOUR LOGGERS
project_logger = _create_root_successor_logger('project')
# DEFINE YOUR LOGGERS ENDS
_echo_init_info()
