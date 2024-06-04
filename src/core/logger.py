import logging
import sys
import os
import colorlog


class Logger:
    def __init__(self):
        self._logger = logging.getLogger(
            "asleep_logging"
        )  # create a logging instance named asleep_logging
        self._logger.setLevel(logging.DEBUG)  # set the level for the logger

        # get the absolute path of the current file
        current_dir = os.path.abspath(os.path.dirname(__file__))
        # go up two directories
        parent_dir = os.path.dirname(os.path.dirname(current_dir))

        file = logging.FileHandler(
            parent_dir + "/logs/asleep.log"
        )  # create a file handler
        stdout = logging.StreamHandler(stream=sys.stdout)  # create a console handler

        file.setLevel(logging.DEBUG)  # set the level for both handlers
        stdout.setLevel(logging.DEBUG)

        formatter = colorlog.ColoredFormatter(  # create a colorized formatter
            "%(log_color)s[%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d]%(reset)s - %(message)s"
        )
        file.setFormatter(formatter)  # set the formatter for both handlers
        stdout.setFormatter(formatter)

        # add the handlers to the logger
        self._logger.addHandler(file)
        self._logger.addHandler(stdout)

    @property
    def logger(self):  # get the logger
        return self._logger
