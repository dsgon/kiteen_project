from core.ui.WebUIElement import WebUIElement as UIElement
from selenium.webdriver.common.by import By

def getFrameOption():
    return UIElement(By.XPATH,'//a[contains(text(),"Frames")]')

def getAlertsOption():
    return UIElement(By.XPATH,'//a[contains(text(),"Alerts")]')

