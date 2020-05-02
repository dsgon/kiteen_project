from core.ui.WebUIElement import WebUIElement as UIElement
from selenium.webdriver.common.by import By

class PythonHomePage():

    def getAboutUs(self):
        return UIElement(By.ID,'about')

    def getQuotes(self):
        return UIElement(By.XPATH,'//a[contains(text(),"Quotes")]')

    def linkLearnMore(self):
        return UIElement(By.CLASS_NAME,'readmore')

    def linkStatus(self):
        return UIElement(By.XPATH,'//a[contains(text(),"Status")]')