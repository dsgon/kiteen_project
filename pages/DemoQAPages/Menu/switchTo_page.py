from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By

def getFrameOption():
    return UIElement(By.XPATH,'//a[contains(text(),"Frames")]')

def getAlertsOption():
    return UIElement(By.XPATH,'//a[contains(text(),"Alerts")]')

