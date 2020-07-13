from core.ui.WebUIElement import WebUIElement as UIElement

class FrameElement(UIElement):

    """
        FrameElement is a class to handler a WebElement that is Parent of other Elements like Frame or iFrames.
        This class inherits from WebUIElement.
    """

    def __init__(self, byType="", locator="", parent=None):
        super().__init__(byType,locator,parent)