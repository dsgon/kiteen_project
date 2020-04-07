from selenium import webdriver
from core.config import ConfigHelper

class WebDriver(object):

    instance = None

    def __init__(self):
        pass

    def getInstance(self):
        if self.instance is None:
            self.createInstance()
        return self.instance

    def createInstance(self):
        if(ConfigHelper.browser == "firefox"):
            firefoxProfile = webdriver.FirefoxProfile()
            firefoxOptions = webdriver.FirefoxOptions()
            if(ConfigHelper.incognito):
                firefoxProfile.set_preference('browser.privatebrowsing.autostart',ConfigHelper.incognito)
            if(ConfigHelper.headless):
                firefoxOptions.set_headless()
            self.instance = webdriver.Firefox(timeout=ConfigHelper.defaultWait,executable_path=ConfigHelper.driverPath,firefox_profile=firefoxProfile,firefox_options=firefoxOptions)
        elif(ConfigHelper.browser == "chrome"):
            chromeoptions = webdriver.ChromeOptions()
            if(ConfigHelper.incognito):
                chromeoptions.add_argument("--incognito")
            if(ConfigHelper.headless):
                chromeoptions.set_headless()
            self.instance = webdriver.Chrome(executable_path=ConfigHelper.driverPath,chrome_options=chromeoptions)
        elif(ConfigHelper.browser == "ie"):
            self.instance = webdriver.Ie(executable_path=ConfigHelper.driverPath,timeout=ConfigHelper.defaultWait)
        elif(ConfigHelper.browser == "edge"):
            self.instance = webdriver.Edge(executable_path=ConfigHelper.driverPath)
        else:
            raise Exception('Invalid Browser')
        self.instance.get(ConfigHelper.urlApp)

