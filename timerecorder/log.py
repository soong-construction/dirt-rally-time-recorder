import logging

def __log_level__(value, levelName):
    logging.addLevelName(value, levelName)
    return value

VERBOSE = __log_level__(5, 'VERBOSE')

GITHUB_ORG = 'https://github.com/soong-construction/'
NAME = 'dirt-rally-time-recorder'

def getProjectUrl():
    return f'{GITHUB_ORG}{NAME}'

def init(filename):
    logFormat = '%(asctime)s %(levelname)s [%(name)s] %(message)s'
    logging.basicConfig(format=logFormat, filename=filename, level=logging.DEBUG)
    logging.log(VERBOSE, 'VERBOSE logging active if this line seen')

def getLogger(module):
    logger = logging.getLogger(module)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(consoleHandler)

    return logger
