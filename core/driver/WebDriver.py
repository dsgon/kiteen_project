from selenium import webdriver
from core.config.ConfigHelper import ConfigHelper


class WebDriver(object):

    """
        Class to handle Selenium driver. This class not requiered an instance.
        To 'create' a instance, call the method 'getInstance()' that return a Singlenton WebDriver
        for all steps requiered.
    """

    __instance = None

    def __init__(self):
        """
            This method doesn't be used! To create/get an instance of WebDriver use 'getInstance()'
            :raise RuntimeError()
        """
        raise RuntimeError('Use getInstance() instead')

    @classmethod
    def getInstance(cls):
        """
            Singleton pattern to create an instance of WebDriver in case that doesn't exist. 
            If exist an instance, return the same.
            :return: WebDriver
        """
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
            cls.__instance.__createInstance(cls)
        return cls.__instance

    def __createInstance(self,cls):
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
            cls.__instance = webdriver.Firefox(timeout=ConfigHelper.getInstance().getDefaultWait(),executable_path=ConfigHelper.getInstance().getDriverPath(),firefox_profile=firefoxProfile,options=firefoxOptions)
        elif(ConfigHelper.getInstance().getBrowser() == "chrome"):
            chromeoptions = webdriver.ChromeOptions()
            if(ConfigHelper.getInstance().getIncognitoMode()):
                chromeoptions.add_argument("--incognito")
            if(ConfigHelper.getInstance().getHeadlessMode()):
                chromeoptions.add_argument("--headless")
            cls.__instance = webdriver.Chrome(executable_path=ConfigHelper.getInstance().getDriverPath(),options=chromeoptions)
        elif(ConfigHelper.getInstance().getBrowser() == "ie"):
            cls.__instance = webdriver.Ie(executable_path=ConfigHelper.getInstance().getDriverPath(),timeout=ConfigHelper.getInstance().getDefaultWait())
        elif(ConfigHelper.getInstance().getBrowser() == "edge"):
            cls.__instance = webdriver.Edge(executable_path=ConfigHelper.getInstance().getDriverPath())
        else:
            raise AttributeError('Invalid Browser')
        cls.__instance.set_page_load_timeout(ConfigHelper.getInstance().getDefaultWait())
        cls.__instance.get(ConfigHelper.getInstance().getUrlApp())

    @classmethod
    def closeDriver(cls):
        """
            A method that close driver and set the instance at None.
        """
        cls.__instance.close()
        cls.__instance=None
