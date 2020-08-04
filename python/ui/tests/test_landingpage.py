#!/usr/bin/python3
import unittest
from python.common.ui.basebrowsertest import BaseBrowserTest
from python.ui.methods.landingpages.landingpage import LandingPage


class TestLandingPage(BaseBrowserTest):
    """"Runs LandingPage based test scenarios."""

    @BaseBrowserTest.log_try_except
    def test_00a_navigate_to_landing_page(self):
        """
        1. Attempt navigate to the landing page.
        """

        the_browser = LandingPage(self.browser)
        the_browser.navigate_to_landing_page()
        value = the_browser.return_header_text()

        assert value == LandingPage.TXT_LANDING_HEADER # This needs to be set to the header text you expect on your application.


if __name__ == '__main__':
    unittest.main()
