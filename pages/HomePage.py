from core.ui.BasePage import BasePage
from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.FrameElement import FrameElement
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    __parentFrame1 = FrameElement(By.ID,'IF1')
    __parents = None

    def getParentFrame1 (self):
        return self.__parentFrame1

    def getSiteDescription_Frame(self):
        return UIElement(By.ID,'site-description',self.__parentFrame1)

    def getSeleniumInJavaOption_Frame(self):
        return UIElement(By.XPATH,'//span[contains(text(),"Selenium in Java")]',self.__parentFrame1)

    def getSeleniumTutotialTitle_Frame(self):
        return UIElement(By.XPATH,'//h1[contains(text(), "Selenium Tutorial")]',self.__parentFrame1)

    def getIFramePracticeOption(self):
        return UIElement(By.XPATH,'//a[contains(text(), "IFrame practice page")]')
        
    def getAboutUs(self):
        return UIElement(By.ID,'about')

    def getQuotes(self):
        return UIElement(By.XPATH,'//a[contains(text(),"Quotes")]')

    def linkLearnMore(self):
        return UIElement(By.CLASS_NAME,'readmore')

    def linkStatus(self):
        return UIElement(By.XPATH,'//a[contains(text(),"Status")]')
