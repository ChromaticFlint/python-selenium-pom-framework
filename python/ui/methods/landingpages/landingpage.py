#!/usr/bin/python3
import time
import python.ui.variables.variables_ui as variables
from python.common.ui.baseclicker import BaseClicker
from selenium.webdriver.common.by import By


class LandingPage(BaseClicker):
    """Class for LandingPage page methods."""

    # Landing Page Assets
    LANDING_HEADER = (By.XPATH, '') # This variable need to be set to your application landing header XPATH.

    # Landing Page Expected Values
    TXT_LANDING_HEADER = '' # This variable needs to be set to what you expect the Landing Header text to return.

    def navigate_to_landing_page(self):

        # Opens a browser and takes in the parameter variables.BASE_URL as the URL.
        self.browser.get(variables.BASE_URL)

        # Waits until the LANDING HEADER is visible.
        self.wait_visible(self.LANDING_HEADER)

    def return_header_text(self) -> str:

        # Waits .5 seconds
        time.sleep(0.5)  # Prevents errors, not being handled by explicit waits.

        # Sets the header_txt variable to the value of LANDING_HEADER text as a string.
        header_txt = self.wait_visible(self.LANDING_HEADER).text

        return header_txt
