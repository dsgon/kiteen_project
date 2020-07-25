from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By

def getOptionAlertOk():
    return UIElement(By.XPATH,'//a[@href="#OKTab"]')

def getOptionAlertOkCancel():
    return UIElement(By.XPATH,'//a[@href="#CancelTab"]')

def getOptionAlertTextbox():
    return UIElement(By.XPATH,'//a[@href="#Textbox"]')

def getButtonAlertOK():
    return UIElement(By.XPATH,'//div[@id = "OKTab"]/button')

def getButtonAlertOKCancel():
    return UIElement(By.XPATH,'//div[@id = "CancelTab"]/button')

def getButtonAlertTextbox():
    return UIElement(By.XPATH,'//div[@id = "Textbox"]/button')

def getMessageText():
    return UIElement(By.ID,'demo1')

