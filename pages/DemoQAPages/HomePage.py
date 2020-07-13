from core.ui.WebUIElement import WebUIElement as UIElement
from selenium.webdriver.common.by import By

def getButtonSkipSingIn():
    return UIElement(By.ID,'btn2')