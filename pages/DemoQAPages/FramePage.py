from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.FrameElement import FrameElement
from selenium.webdriver.common.by import By

class FramePage():

    __parentFrame1 = FrameElement(By.ID,'singleframe')

    __parentFrame2_1 = FrameElement(By.XPATH,'//div[@id = "Multiple"]/iframe')
    __parentFrame2_2 = FrameElement(By.XPATH,'//iframe',__parentFrame2_1)

    def getButtonIframeWithIframe(self):
        return UIElement(byType=By.XPATH,locator='//a[contains(text(),"Iframe with in an Iframe")]')

    def getSingleInput(self):
        return UIElement(byType=By.XPATH,locator='//input',parentFrame=self.__parentFrame1)

    def getInputInFrames(self):
        return UIElement(byType=By.XPATH,locator='//input',parentFrame=self.__parentFrame2_2)

    