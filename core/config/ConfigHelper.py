from Lib import json

browser = None
driverPath = None
urlApp = None
defaultWait = None
incognito = False
headless = False

with open('./config.json') as configFile:
    config = json.load(configFile)
    browser = config['browser']
    driverPath = config['driverPath']
    urlApp = config['urlApp']
    defaultWait = config['defaultWait']
    incognito = config['incognito']
    headless = config['headless']
