import logging

def __log_level__(value, levelName):
    logging.addLevelName(value, levelName)
    return value

VERBOSE = __log_level__(5, 'VERBOSE')
logFormat = '%(asctime)s %(levelname)s [%(name)s] %(message)s'

def init(filename):
    logging.basicConfig(format=logFormat, filename=filename, level=VERBOSE)

def getLogger(module):
    logger = logging.getLogger(module)
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(consoleHandler)
    
    return logger