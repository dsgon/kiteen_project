from Lib.abc import ABC

from core.driver.WebDriver import WebDriver
from core.config import ConfigHelper

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import StaleElementReferenceException , WebDriverException, NoSuchElementException, TimeoutException

from Lib import traceback
import time

class BaseElement (ABC):

    __element = None
    __byType = None
    __parentFrame = None

    def __getDriver(self):
        """
            Call for the instance of WebDriver to return it.
            @return WebDriver
        """
        return WebDriver.getInstance()

    def __getDriverWait(self):
        """
            Call for Selenium WebDriver Wait to create a handle of elements with a wait. This wait is configured in the file config.json
            @return WebDriverWait
        """
        return WebDriverWait(self.__getDriver(),ConfigHelper.defaultWait)

    def __get(self, withWait=False):
        """
            Finds a element of current page.
            If this element has not withWait find it via find_element else will set on True the search with wait
            and will search the element with expected_conditions.presence_of_element_located.

            @param withWait : bool (Default value is False)
            @return WebElement
        """
        tryCount = 0
        maxTries = 6
        while (tryCount <= maxTries):
            try:
                if (withWait == False):
                    return self.__getDriver().find_element(self._BaseElement__byType,self._BaseElement__element)
                else:
                    return self.__getDriverWait().\
                        until(expected_conditions.presence_of_element_located((self._BaseElement__byType,self._BaseElement__element)))
            except StaleElementReferenceException:
                print("Stale Element Reference Exception: " + self._BaseElement__element)
                time.sleep(0.5)
            except NoSuchElementException:
                print("No Such Element: " + self._BaseElement__element)
                time.sleep(0.5)
            tryCount+=1
        return None

    def __exist(self, withWait=True, visible=False):
        """
            Indicate if an element is present or visible on the current page.
            This method use a default value to withWait param to wait for this element (value = True).
            
            The visible value is a flag to find the current element  presence (visible=False) or visibility (visible=True)

            @param withWait : bool
            @param visible : bool
            @return bool
        """
        exists = False
        parentsFrame = None
        self.__getDriver().switch_to.default_content()
        try:
            if (not withWait):
                if(not self.hasParent()):
                    exists = self.__get() != None
                else:
                    if(not self.__parentFrame.hasParent()):
                        if(parentsFrame==None):
                            self.__getDriver().switch_to.frame(self.__parentFrame.__get())
                            exists = self.__get() != None
                        else:
                            for parent in parentsFrame:
                                parent.__exist()
                                parent.__getDriver().switch_to.frame(self.__parentFrame.__get())
                    else:
                        parentsFrame.append(self.__parentFrame)
                        self.__parentFrame.__exist()
            else:
                if(not self.hasParent()):
                    if(not visible):
                        exists = self.__getDriverWait().until(expected_conditions.\
                            presence_of_element_located((self._BaseElement__byType,self._BaseElement__element))) != None
                    else:
                        exists = self.__getDriverWait().until(expected_conditions.\
                            visibility_of_element_located((self._BaseElement__byType,self._BaseElement__element))) != None
                else:
                    if(not self.__parentFrame.hasParent()):
                        if(parentsFrame==None):
                            if(not visible):
                                self.__getDriver().switch_to.frame(self.__parentFrame.__get())
                                exists = self.__getDriverWait().until(expected_conditions.\
                                    presence_of_element_located((self._BaseElement__byType,self._BaseElement__element))) != None
                            else:
                                exists = self.__getDriverWait().until(expected_conditions.\
                                    visibility_of_element_located((self._BaseElement__byType,self._BaseElement__element))) != None
                        else:
                            for parent in parentsFrame:
                                parent.__exist()
                                parent.__getDriver().switch_to.frame(self.__parentFrame.__get())
                    else:
                        parentsFrame.append(self.__parentFrame)
                        self.__parentFrame.__exist()
                
        except NoSuchElementException:
           print("No Such Element: " + self._BaseElement__element)
        except TimeoutException:
            print("TimeOutException: Unable to find element <"+self._BaseElement__element+"> in "+str(ConfigHelper.defaultWait)+" seg")
            traceback.print_exc()
        return exists

    def hasParent(self):
        if (self.__parentFrame == None):
            return False
        else:
            return True