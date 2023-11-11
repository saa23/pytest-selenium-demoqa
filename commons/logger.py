import logging

# create logger instance
logger_instance = logging.getLogger(__name__)
logger_instance.setLevel(level=logging.INFO)
formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(module)s(line: %(lineno)d): %(message)s'
                              , "%Y-%m-%d %H:%M:%S")

# create streamHandler instance
streamer = logging.StreamHandler()
streamer.setLevel(level=logging.INFO)
streamer.setFormatter(formatter)
logger_instance.addHandler(streamer)
