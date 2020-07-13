from core.ui.WebUIElement import WebUIElement as UIElement
from selenium.webdriver.common.by import By

def getOptionSwitchTo():
    return UIElement(By.XPATH,'//a[contains(text(),"SwitchTo")]')

