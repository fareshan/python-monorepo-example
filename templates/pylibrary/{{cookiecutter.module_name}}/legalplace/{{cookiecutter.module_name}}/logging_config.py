"""a common logging config for all files"""

import logging.config


class LevelOnlyFilter:
    """filter to show only selected level logs"""

    def __init__(self, level):
        self.level = level

    def filter(self, record):
        """filter to show only selected level logs"""
        return record.levelno == self.level


LOGGING_CONFIG = {
    "version": 1,
    "loggers": {
        "": {  # root logger
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["stream_handler", "file_handler"],
        },
        "custom_logger": {
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["stream_handler"],
        },
    },
    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "DEBUG",
            # "filters": ["only_warning"],
            "formatter": "colored_formatter",
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "filename": "output.log",
            "mode": "w",
            "level": "DEBUG",
            "formatter": "default_formatter",
        },
    },
    "filters": {
        "only_warning": {
            "()": LevelOnlyFilter,
            "level": logging.WARN,
        },
    },
    "formatters": {
        "default_formatter": {
            "format": "%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d",
            "datefmt": "%y-%m-%d %I:%M:%S %p",
        },
        "colored_formatter": {
            # https://docs.python.org/3/library/logging.html#logrecord-attributes
            "format": "%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d",
            "datefmt": "%y-%m-%d %I:%M:%S %p",
            "()": "coloredlogs.ColoredFormatter",  # Adds colors to logs
        },
    },
}

# Run once at startup:
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
logger.info("logger config")
