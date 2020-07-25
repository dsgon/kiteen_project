from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By

def getOptionSwitchTo():
    return UIElement(By.XPATH,'//a[contains(text(),"SwitchTo")]')

