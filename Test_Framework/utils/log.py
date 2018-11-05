#!/usr/bin/python3
# -*- coding:utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler
from .config import Config
from .config import LOG_PATH


class Logger(object):
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        log_obj = Config().get('log', 2)
        self.log_file_name = log_obj.get('file_name')
        self.backup_count = log_obj.get('backup')

        # log output level
        self.console_output_level = log_obj.get('console_level')
        self.file_output_level = log_obj.get('file_level')

        # log output format
        self.formatter = logging.Formatter(log_obj.get('pattern'))

    def get_logger(self):
        if not self.logger.handlers:        # avoid duplicate log
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # generate one log file for one day, only keep backup_count logs
            file_handler = TimedRotatingFileHandler(filename=LOG_PATH + '\\' + self.log_file_name,
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger
logger = Logger().get_logger()


