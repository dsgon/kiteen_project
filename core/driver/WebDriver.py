from selenium import webdriver
from core.config import ConfigHelper

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
            @return WebDriver
        """
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
            cls.__instance.__createInstance(cls)
        return cls.__instance

    def __createInstance(self,cls):
        """
            This method creates an instance of WebDriver.
            This Webdriver is created with the settings that contain the file 'config.json'
            @param cls : WebDriver
        """
        if(ConfigHelper.browser == "firefox"):
            firefoxProfile = webdriver.FirefoxProfile()
            firefoxOptions = webdriver.FirefoxOptions()
            if(ConfigHelper.incognito):
                firefoxProfile.set_preference('browser.privatebrowsing.autostart',ConfigHelper.incognito)
            if(ConfigHelper.headless):
                firefoxOptions.set_headless()
            cls.__instance = webdriver.Firefox(timeout=ConfigHelper.defaultWait,executable_path=ConfigHelper.driverPath,firefox_profile=firefoxProfile,options=firefoxOptions)
        elif(ConfigHelper.browser == "chrome"):
            chromeoptions = webdriver.ChromeOptions()
            if(ConfigHelper.incognito):
                chromeoptions.add_argument("--incognito")
            if(ConfigHelper.headless):
                chromeoptions.add_argument("--headless")
            cls.__instance = webdriver.Chrome(executable_path=ConfigHelper.driverPath,options=chromeoptions)
        elif(ConfigHelper.browser == "ie"):
            cls.__instance = webdriver.Ie(executable_path=ConfigHelper.driverPath,timeout=ConfigHelper.defaultWait)
        elif(ConfigHelper.browser == "edge"):
            cls.__instance = webdriver.Edge(executable_path=ConfigHelper.driverPath)
        else:
            raise Exception('Invalid Browser')
        cls.__instance.set_page_load_timeout(ConfigHelper.defaultWait)
        cls.__instance.get(ConfigHelper.urlApp)

    @classmethod
    def closeDriver(cls):
        """
            A method that close driver and set the instance at None.
        """
        cls.__instance.close()
        cls.__instance=None
