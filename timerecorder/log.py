import logging

def __log_level__(value, levelName):
    logging.addLevelName(value, levelName)
    return value

VERBOSE = __log_level__(5, 'VERBOSE')
logFormat = '%(asctime)s %(levelname)s [%(name)s] %(message)s'

gitHubOrg = 'https://github.com/soong-construction/'
name = 'dirt-rally-time-recorder'

def getProjectUrl():
    return '%s%s' % (gitHubOrg, name)

def init(filename):
    logging.basicConfig(format=logFormat, filename=filename, encoding='utf-8', level=logging.DEBUG)
    logging.log(VERBOSE, 'VERBOSE logging active if this line seen')

def getLogger(module):
    logger = logging.getLogger(module)
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(consoleHandler)
    
    return logger
