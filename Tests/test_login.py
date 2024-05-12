import time
from selenium.webdriver import ActionChains
from Pages.HomePage import homePage
from Pages.LoginPage import LoginPage
from Utilities.baseClass import BaseClass


class Test_login(BaseClass):

    def test_login(self):
        print(self.read_testdata_from_excel())
        home_page = homePage(self.driver)
        login_page = LoginPage(self.driver)
        Account_Lists = self.check_visibility_of_element(home_page.Account_lists)
        action = ActionChains(self.driver)
        time.sleep(6)
        action.move_to_element(Account_Lists).perform()
        click_login = self.element_to_be_clickable(home_page.login_btn)
        click_login.click()
        email_mobile = self.element_to_be_clickable(login_page.email_mobile)
        email_mobile.send_keys("ranju@gmail.com")
        continue_btn = self.element_to_be_clickable(login_page.continue_btn)
        continue_btn.click()
        password = self.element_to_be_clickable(login_page.password)
        password.send_keys("ranju2345")
        sign_in = self.element_to_be_clickable(login_page.sign_in)
        sign_in.click()
        # try:
        #     print(self.read_testdata_from_excel())
        #     home_page = homePage(self.driver)
        #     login_page = LoginPage(self.driver)
        #     Account_Lists = self.check_visibility_of_element(home_page.Account_lists)
        #     action = ActionChains(self.driver)
        #     time.sleep(6)
        #     action.move_to_element(Account_Lists).perform()
        #     click_login = self.element_to_be_clickable(home_page.login_btn)
        #     click_login.click()
        #     email_mobile = self.element_to_be_clickable(login_page.email_mobile)
        #     email_mobile.send_keys("ranju@gmail.com")
        #     continue_btn = self.element_to_be_clickable(login_page.continue_btn)
        #     continue_btn.click()
        #     password = self.element_to_be_clickable(login_page.password)
        #     password.send_keys("ranju2345")
        #     sign_in = self.element_to_be_clickable(login_page.sign_in)
        #     sign_in.click()
        # except Exception as err:
        #     print("Error", err)




