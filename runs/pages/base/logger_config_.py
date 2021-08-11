import inspect
import logging
import datetime


def get_log_time():
    log_start_time = str(datetime.datetime.now()).replace(' ', '_')\
        .replace('.', '_')\
        .replace(':', '-')

    return log_start_time


def logger_config_(log_level=logging.DEBUG):
    timed = False
    logger_time = None

    if not timed:
        logger_time = get_log_time()
        timed = True

    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(filename=".\\logs\\" + logger_time[:-10] + "_automation.log", mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def warn(msg): logger_config_().warning(msg)


def info(msg): logger_config_().info(msg)


def err(msg): logger_config_().info(msg)


def exc(msg): logger_config_().exception(msg)


def crit(msg): logger_config_().critical(msg)

