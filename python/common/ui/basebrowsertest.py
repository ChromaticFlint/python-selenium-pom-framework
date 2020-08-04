#!/usr/bin/python3
from selenium import webdriver
from python.common.baseunittest import BaseUnitTest


class BaseBrowserTest(BaseUnitTest):
    """Shared parent base class for UI tests. Adds onto BaseUnitTest."""

    def setUp(self):
        """Open browser."""

        super().setUp()
        self.browser = webdriver.Chrome()
        self.browser.set_window_position(0, 0)  # Puts browser in front.
        self.browser.set_window_size(1280, 800)

    def tearDown(self):
        """Quit browser."""

        super().tearDown()
        self.browser.quit()
