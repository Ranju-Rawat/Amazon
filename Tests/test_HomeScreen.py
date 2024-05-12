import time

import pytest
import requests

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions

from Pages.HomePage import homePage
from Utilities.baseClass import BaseClass


class Test_homeScreen(BaseClass):
    driver = None

    @pytest.mark.imp
    def test_verifyWebsite(self):
        log = self.create_log_file()
        try:
            title = self.driver.title
            assert "Shopping" in title, "Actual Result does not have Online Shopping"
            print(title)
        except Exception as err:
            print(f"Error in test_verifyWebsite : {str(err)}")
            log.critical(str(err))
            screenshot = "C:\\Users\\rawat\\PycharmProjects\\Amazon\\Amazon\\Reports\\verifyWebsite.png"
            self.driver.get_screenshot_as_file(screenshot)

    @pytest.mark.skip
    def test_verifySearchProducts(self):
        HomePage = homePage(self.driver)
        log = self.create_log_file()
        try:
            search_Product = self.element_to_be_clickable(HomePage.Search_Product)
            search_Product.send_keys("dress")
            search_Product.send_keys(Keys.ENTER)
            match_msg = self.check_visibility_of_element(HomePage.Result_msg)
            assert "dress" in match_msg.text, "Actual Result does not have dress"


        except Exception as error:
            print(f"Error in test_verifySearchProducts : {str(error)}")
            log.error(str(error))
            screenshot = "C:\\Users\\rawat\\PycharmProjects\\Amazon\\Amazon\\Reports\\SearchResult.png"
            self.driver.get_screenshot_as_file(screenshot)

    # def test_verify_links(self):
    #     home_page = homePage(self.driver)
    #     link_list = self.get_multiple_elements(home_page.links)
    #     for link in link_list:
    #         url = link.get_attribute("href")
    #         if url is None:
    #             print("Skipping because url is None")
    #             continue
    #         try:
    #             result = requests.head(url)
    #             print("lnks", result)
    #             if result.status_code == 200:
    #                 print("URL is valid")
    #             else:
    #                 print("broken links", result.status_code)
    #         except Exception as error:
    #             print("error", error)
