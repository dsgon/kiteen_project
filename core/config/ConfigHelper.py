from Lib import json

class ConfigHelper:

    """
        Class to get parameters from the config.json file.
        This class implements a Singleton Pattern.
    """

    __instance = None
    __config = None
    __browser = None
    __driverPath = None
    __urlApp = None
    __defaultWait = None
    __incognito = False
    __headless = False

    @staticmethod
    def getInstance():
        """
            Singleton Pattern to create an instance from ConfigHelper. 
            If the instance doesn't exist this method call to create it. Otherwise, It returns it.
            
            :return: ConfigHelper
        """
        if ConfigHelper.__instance == None:
            ConfigHelper().__loadParameters()
        return ConfigHelper.__instance

    def __init__(self):
        """
            Constructor to set the private variable __instance into self.
            If this constructor is called and __instance exists, It will raise a NotImplementedError

            :raise: NotImplementedError
        """
        if ConfigHelper.__instance != None:
            raise NotImplementedError("This is a Singlenton Class")
        ConfigHelper.__instance = self


    def __loadParameters(self):
        """
            Loads all parameters from the config.json file
        """
        with open('./config.json') as configFile:
            self.__config = json.load(configFile)
            self.__browser = self.__config['browser']
            self.__driverPath = self.__config['driverPath']
            self.__urlApp = self.__config['urlApp']
            self.__defaultWait = self.__config['defaultWait']
            self.__incognito = self.__config['incognito']
            self.__headless = self.__config['headless']

    def setUrlApp(self, url):
        self.__urlApp = url

    def setDefaultUrlApp(self):
        self.__urlApp = self.__config['urlApp']

    def getUrlApp(self):
        return self.__urlApp
    
    def getBrowser(self):
        return self.__browser

    def getDriverPath(self):
        return self.__driverPath

    def getDefaultWait(self):
        return self.__defaultWait

    def getIncognitoMode(self):
        return self.__incognito

    def getHeadlessMode(self):
        return self.__headless