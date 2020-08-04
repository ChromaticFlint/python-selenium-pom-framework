#!/usr/bin/python3
from selenium.webdriver.support.ui import WebDriverWait
from python.common.baselogger import BaseLogger
from selenium.webdriver.support import expected_conditions as EC


class BaseClicker(object):
    """Shared parent class for UI actions."""

    # This needs to be out here, to ensure it is only called ONCE across all
    #   instances of the class.
    log = BaseLogger()

    def __init__(self, driver):
        self.browser = driver

    def find(self, obj):
        """
        Finds the WebElement. Use for speed.

            :param obj: the object to find, as (By.X, path).
            :return: the WebElement object.
        """
    
        return self.browser.find_element(*obj)

    def wait_multiple(self, obj1, obj2):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(obj1) or EC.visibility_of_element_located(obj2))
            
    def wait_visible(self, obj):
        """
        Explicit wait for the WebElement to be visible. Use when need to wait
            for element.

            :param obj: the object to wait for, as (By.X, path).
            :return: the WebElement object.
        """

        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(obj))

    def wait_clickable(self, obj):
        """
        Explicit wait for the WebElement to be click-able. Use when need to wait
            for element to be interact-able.

            :param obj: the object to wait for, as (By.X, path).
            :return: the WebElement object.
        """

        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(obj))
