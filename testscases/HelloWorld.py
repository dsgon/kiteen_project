import unittest
from core.driver import WebDriver
from core.config import ConfigHelper


class HelloWorld(unittest.TestCase):

    
    def setUp(self):
        ConfigHelper
        self.driver = WebDriver.WebDriver().getInstance()

    def test_home_screen(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
