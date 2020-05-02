import pytest
from steps.PythonSteps.HomeSteps import PythonHomeSteps

expectedTitle = 'About Python™ | Python.org'

@pytest.mark.smoke
def test_click_withWait():
    PythonHomeSteps().clickOnAboutUs(True).verifyPageTitle(expectedTitle).takeScreenshot()

def test_click_withoutWait():
    PythonHomeSteps().clickOnAboutUs(False).verifyPageTitle(expectedTitle).takeScreenshot()

@pytest.mark.smoke
def test_mouse_over():
    PythonHomeSteps().verifyAboutUsButton().mouseOnAboutUs().takeScreenshot()

@pytest.mark.smoke
def test_scroll_until():
    PythonHomeSteps().moveUntilStatusLink().verifyStatusLinkIsVisible().takeScreenshot()

@pytest.mark.smoke
def test_verify_element_present():
    PythonHomeSteps().verifyStatusLinkIsPresent().takeScreenshot()

def teardown():
    PythonHomeSteps().closeBrowser()