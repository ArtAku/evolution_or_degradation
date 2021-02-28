import logging
from configurator import logger_config

_log_format = f"%(asctime)s|%(levelname)s|%(filename)s/%(funcName)s|%(message)s"

def get_file_handler(name):
  file_handler = logging.FileHandler(name)
  file_handler.setLevel(logger_config['FILE_LOG_LEVEL'])
  file_handler.setFormatter(logging.Formatter(_log_format))
  file_handler.name = 'file_log'
  return file_handler

def get_stream_handler():
  stream_handler = logging.StreamHandler()
  stream_handler.setLevel(logger_config['CONSOLE_LOG_LEVEL'])
  stream_handler.setFormatter(logging.Formatter(_log_format))
  stream_handler.name = 'stream_log'
  return stream_handler

def get_logger(name, filename=logger_config['FILE_LOG_NAME']):
  logger = logging.getLogger(name)
  logger.setLevel(logging.DEBUG)
  logger.addHandler(get_file_handler(filename))
  logger.addHandler(get_stream_handler())
  return logger