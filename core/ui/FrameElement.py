from core.ui.WebUIElement import WebUIElement as UIElement

class FrameElement(UIElement):

    def __init__(self, byType, locator, parent=None):
        self._BaseElement__byType = byType
        self._BaseElement__element = locator
        self._BaseElement__parentFrame = parent