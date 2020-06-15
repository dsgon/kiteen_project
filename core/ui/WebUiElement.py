from core.ui.BaseElement import BaseElement

from selenium.webdriver.common.action_chains import ActionChains

class WebUIElement (BaseElement):

    """
        Class to handle the Selenium WebElement.
        This class offer all methods of WebElement with exception handle.
        This class inherits from BaseElement.
    """

    def __init__(self, byType, locator, parentFrame=None):
        """
            WebUIElement constructor receives a By object and a locator string to perform actions over this element 
            and a parentFrame.
            @param byTipe : By
            @param locator: str
            @param parentFrame : List<FrameElement>
        """
        self._BaseElement__byType = byType
        self._BaseElement__element = locator
        self._BaseElement__parentFrame = parentFrame

    def click(self, withWait=False):
        """
            Perform a click action over the current element.
        """
        self._BaseElement__get(withWait).click() 

    def isDisplayed(self):
        """
            Search for the visibility of the current element.
            @return : bool
        """
        return self._BaseElement__exist(visible=True)

    def isPresent(self):
        """
            Search for the presence of the current element.
            @return : bool
        """
        return self._BaseElement__exist()

    def mouseOver(self):
        """
            Perform a 'mouse over' the current element. This element must be visible on the screen.
            This method doesn't work on Internet Explorer
        """
        action = ActionChains(self._BaseElement__getDriver()).move_to_element(self._BaseElement__get())
        action.perform()

    def submit(self):
        """
            Perform the submit action in the current element. 
            If this element is part of a form this action will send the current form like the button submit has been clicked
        """
        self._BaseElement__get().submit()

    def clear(self):
        """
            Clear a textbox field
        """
        self._BaseElement__get().clear()

    def setText(self, text):
        """
            Send the text receive into a textbox
            @param text : str
        """
        self._BaseElement__get().send_keys(text)

    def getText(self):
        """
            Get the text of a element
            @return str
        """
        return self._BaseElement__get().text

    def scrollUntilThis(self):
        """
            Perform the scroll action until the visibility of current element
        """
        self._BaseElement__getDriver().execute_script("arguments[0].scrollIntoView();", self._BaseElement__get())

    def clickByJavaScript(self):
        """
            Perform a click action over the current element using JavaScript
        """
        self._BaseElement__getDriver().execute_script("arguments[0].click();",self._BaseElement__get())
