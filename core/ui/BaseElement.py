from Lib.abc import ABC

from core.driver.WebDriver import WebDriver
from core.config.ConfigHelper import ConfigHelper

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import StaleElementReferenceException , WebDriverException, NoSuchElementException, TimeoutException

from Lib import traceback
import time


class BaseElement (ABC):

    """
        BaseElement is an Abstract class that offers some methods to perform wait actions on Driver and return the result.
    """

    __element = None
    __byType = None
    __parentFrame = None
    __parentsList = []
    
    def __getDriver(self):
        """
            Call for the instance of WebDriver to return it.
            :return: WebDriver
        """
        return WebDriver.getInstance()

    def __getDriverWait(self):
        """
            Call for Selenium WebDriver Wait to create a handle of elements with a wait. This wait is configured in the file config.json
            :return: WebDriverWait
        """
        return WebDriverWait(self.__getDriver(),ConfigHelper.getInstance().getDefaultWait())

    def __get(self, withWait=False):
        """
            Finds a element of current page.
            If this element has not withWait find it via find_element else will set on True the search with wait
            and will search the element with expected_conditions.presence_of_element_located.

            :param withWait: bool
            :return: WebElement
        """
        tryCount = 0
        maxTries = 6
        while (tryCount < maxTries):
            self.__getDriver().switch_to.default_content()
            try:
                if (withWait == False):
                    if (not self.hasParent()):
                        return self.__getDriver().find_element(self.__byType,self.__element)
                    else:
                        if(not self.__parentFrame.hasParent()):
                            self.__getDriver().switch_to.frame(self.__parentFrame.__get())
                            return self.__getDriver().find_element(self.__byType,self.__element)
                        else:
                            parents = []
                            element = self
                            
                            while(element.hasParent()):        
                                element = element.__parentFrame
                                parents.append(element)

                            parents.reverse()

                            for parent in parents:
                                self.__getDriver().switch_to.frame(self.__getDriver().find_element(parent.__byType,parent.__element))

                            element = self.__getDriver().find_element(self.__byType,self.__element)

                            return element
                else:
                    if (not self.hasParent()):
                        return self.__getDriverWait().\
                            until(expected_conditions.presence_of_element_located((self._BaseElement__byType,self._BaseElement__element)))
                    else:
                        if(not self.__parentFrame.hasParent()):
                            self.__getDriver().switch_to.frame(self.__parentFrame.__get())
                            return self.__getDriverWait().\
                            until(expected_conditions.presence_of_element_located((self._BaseElement__byType,self._BaseElement__element)))
                        else:
                            parents = []
                            parent = self.__parentFrame

                            while(parent.hasParent()):
                                parents.append(parent)
                                parent = parent.__parentFrame
                            for parent in parents:
                                self.__getDriver().switch_to.frame(parent.__get())

                            element = self.__getDriverWait().\
                                    until(expected_conditions.presence_of_element_located((self._BaseElement__byType,self._BaseElement__element)))
                            
                            for parent in parents:
                                self.__getDriver().switch_to.default_content()
                            return element
                        
            except StaleElementReferenceException as ser:
                print("Stale Element Reference Exception: {}\n{}".format(self._BaseElement__element,ser))
                time.sleep(0.5)
            except NoSuchElementException as se:
                print("No Such Element: {}\n{}".format(self._BaseElement__element, se.with_traceback))
                time.sleep(0.5)
            tryCount+=1
        return None

    def __exist(self, withWait=True, visible=False):
        """
            Indicate if an element is present or visible on the current page.
            This method use a default value to withWait param to wait for this element (value = True).
            
            The visible value is a flag to find the current element  presence (visible=False) or visibility (visible=True)

            :param withWait: bool
            :param visible: bool
            :return: bool
        """
        exists = False
        
        self.__getDriver().switch_to.default_content()
        try:
            if (not withWait):
                if(not self.hasParent()):
                    exists = self.__get() != None
                else:
                    if(not self.__parentFrame.hasParent()):
                        #TO-DO: Check me!
                        if(len(self._BaseElement__parentsList)==0):
                            self.__getDriver().switch_to.frame(self.__parentFrame.__get())
                            exists = self.__get() != None
                        else:
                            for parent in self._BaseElement__parentsList:
                                parent.__exist()
                                parent.__getDriver().switch_to.frame(self.__parentFrame.__get())
                    else:
                        #TO-DO: Check me!
                        self._BaseElement__parentsList.append(self.__parentFrame)
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
                        if(not visible):
                            self.__getDriver().switch_to.frame(self.__parentFrame.__get(withWait=True))
                            exists = self.__getDriverWait().until(expected_conditions.\
                                presence_of_element_located((self._BaseElement__byType,self._BaseElement__element))) != None
                        else:
                            self.__getDriver().switch_to.frame(self.__parentFrame.__get(withWait=True))
                            exists = self.__getDriverWait().until(expected_conditions.\
                                visibility_of_element_located((self._BaseElement__byType,self._BaseElement__element))) != None
                    else:
                        parents = []
                        parent = self.__parentFrame
                        while(parent.hasParent()):
                            parents.append(parent)
                            parent = parent.__parentFrame
                        for parent in parents:
                            self.__getDriver().switch_to.frame(parent.__get(withWait=True))

                        exists = self.__getDriverWait().until(expected_conditions.\
                                    visibility_of_element_located((self._BaseElement__byType,self._BaseElement__element))) != None
                
        except NoSuchElementException:
           print("No Such Element: {}".format(self._BaseElement__element))
        except TimeoutException:
            print("TimeOutException: Unable to find element <{}> in {} seg".format(self._BaseElement__element,ConfigHelper.getInstance().getDefaultWait()))
            traceback.print_exc()
        self.__getDriver().switch_to.default_content()
        return exists

    def hasParent(self):
        """
            Verify if the current element has a Parent element (Frame Element)
        """
        if (self.__parentFrame == None):
            return False
        else:
            return True