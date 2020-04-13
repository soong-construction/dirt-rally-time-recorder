import logging

def __log_level__(value):
    return value

VERBOSE = __log_level__(5)

logging.basicConfig(format='%(asctime)s %(levelname)s [%(name)s] %(message)s', filename='timerecord.log', level=logging.DEBUG)

def getLogger(module):
    logger = logging.getLogger(module)
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(consoleHandler)
    
    return logger