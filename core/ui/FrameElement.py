from core.ui.WebUIElement import WebUIElement as UIElement

class FrameElement(UIElement):

    """
        FrameElement is a class to handler a WebElement that is Parent of other Elements like Frame or iFrames.
        This class inherits from WebUIElement.
    """

    def __init__(self, byType, locator, parent=None):
        self._BaseElement__byType = byType
        self._BaseElement__element = locator
        self._BaseElement__parentFrame = parent