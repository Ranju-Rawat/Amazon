from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from Pages.AmzFreshGroceriesPage import FreshGroceries
from Pages.HomePage import homePage
from Utilities.baseClass import BaseClass


class Test_freshGroceries(BaseClass):

    driver = None

    def test_open_PearFruit(self):
        home_page = homePage(self.driver)
        groceries_page = FreshGroceries(self.driver)
        fresh_btn = self.check_visibility_of_element(home_page.fresh)
        action = ActionChains(self.driver)
        action.move_to_element(fresh_btn).perform()
        click_on_fresh = self.element_to_be_clickable(home_page.fresh_groceries_btn)
        click_on_fresh.click()
        skip_location_box = self.element_to_be_clickable(groceries_page.skip_location)
        print(skip_location_box)

        # element = self.check_visibility_of_element(groceries_page.fruits_veg)
        # self.driver.execut_script("arguments[0].scrollIntoView(true)", element)


