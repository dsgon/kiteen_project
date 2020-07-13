from core.config.ConfigHelper import ConfigHelper
from selenium import webdriver

class FactoryDriver():

    __driver = None

    def createDriver(self):
        """
            This method creates an instance of WebDriver.
            This Webdriver is created with the settings that contain the file 'config.json'
            :param: WebDriver
        """
        if(ConfigHelper.getInstance().getBrowser() == "firefox"):
            firefoxProfile = webdriver.FirefoxProfile()
            firefoxOptions = webdriver.FirefoxOptions()
            firefoxProfile.set_preference('browser.privatebrowsing.autostart',ConfigHelper.getInstance().getIncognitoMode())
            firefoxOptions.headless = ConfigHelper.getInstance().getHeadlessMode()
            self.__driver = webdriver.Firefox(timeout=ConfigHelper.getInstance().getDefaultWait(),executable_path=ConfigHelper.getInstance().getDriverPath(),firefox_profile=firefoxProfile,options=firefoxOptions)
        elif(ConfigHelper.getInstance().getBrowser() == "chrome"):
            chromeoptions = webdriver.ChromeOptions()
            if(ConfigHelper.getInstance().getIncognitoMode()):
                chromeoptions.add_argument("--incognito")
            if(ConfigHelper.getInstance().getHeadlessMode()):
                chromeoptions.add_argument("--headless")
            self.__driver = webdriver.Chrome(executable_path=ConfigHelper.getInstance().getDriverPath(),options=chromeoptions)
        elif(ConfigHelper.getInstance().getBrowser() == "ie"):
            self.__driver = webdriver.Ie(executable_path=ConfigHelper.getInstance().getDriverPath(),timeout=ConfigHelper.getInstance().getDefaultWait())
        elif(ConfigHelper.getInstance().getBrowser() == "edge"):
            self.__driver = webdriver.Edge(executable_path=ConfigHelper.getInstance().getDriverPath())
        else:
            raise AttributeError('Invalid Browser')
        self.__driver.maximize_window()
        self.__driver.get(ConfigHelper.getInstance().getUrlApp())
        self.__driver.set_page_load_timeout(ConfigHelper.getInstance().getDefaultWait())
        
        return self.__driver