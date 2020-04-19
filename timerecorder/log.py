import logging

def __log_level__(value):
    return value

VERBOSE = __log_level__(5)
logFormat = '%(asctime)s %(levelname)s [%(name)s] %(message)s'

def init(filename):
    logging.basicConfig(format=logFormat, filename=filename, level=logging.DEBUG)

def getLogger(module):
    logger = logging.getLogger(module)
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(consoleHandler)
    
    return logger