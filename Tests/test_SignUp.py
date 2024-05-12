import time
import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from Pages.HomePage import homePage
from Pages.SignUpPage import SignUpPage
from Pages.VerificationPage import verification_Page
from Utilities.baseClass import BaseClass


class Test_SignUp(BaseClass):
    driver = None

    def test_SignUpForm(self):
        home_page = homePage(self.driver)
        sign_page = SignUpPage(self.driver)
        log = self.create_log_file()
        try:
            Account_Lists = self.check_visibility_of_element(home_page.Account_lists)
            action = ActionChains(self.driver)
            time.sleep(6)
            action.move_to_element(Account_Lists).perform()
            Sign_up_button = self.element_to_be_clickable(sign_page.sign_up_button)
            Sign_up_button.click()
            title = self.driver.title
            assert "Registration" in title, "Actual Result does not have Registration"

        except NoSuchElementException as e:
            self.handle_exceptions(log, e, "SignUpButton_Click")

        except TimeoutException as e:
            self.handle_exceptions(log, e, "Timeout_waiting_for_element")

        except AssertionError as e:
            self.handle_exceptions(log, e, "Assertion_error")

        except Exception as e:
            self.handle_exceptions(log, e, "Generic_error")

    def test_VerifyEmptyFormValidation(self):
        sign_up_page = SignUpPage(self.driver)
        log = self.create_log_file()
        try:
            verify_mob_btn = self.element_to_be_clickable(sign_up_page.verify_mobile_number)
            verify_mob_btn.click()
            error_Msgs = self.get_multiple_elements(sign_up_page.error_msgs)
            for err in error_Msgs:
                if err.text != "":
                    assert "name" or "number" or "password" in err.text

        except Exception as error:
            self.handle_exceptions(log, error, "EmptyFormValidation")

    def test_Verify_Valid_Form_Submission(self):
        # self.driver.set_window_size(500, 500)
        self.write_to_textFile("Utilities/usrData.txt", "w")
        usr_data = self.read_textFile("Utilities/usrData.txt", "r")
        #usr_data = [line.rstrip() for line in data]
        #time.sleep(4)

        # self.write_to_textFile("Utilities/sign_up_data.txt", "w")
        sign_up_page = SignUpPage(self.driver)
        log = self.create_log_file()
        try:
            Usr_Name = self.element_to_be_clickable(sign_up_page.user_name)
            Usr_Name.send_keys(usr_data[0])
            dropdown = self.element_to_be_clickable(sign_up_page.click_country_dropdown)
            # dropdown.click()
            # dropdown_list = self.get_multiple_elements(sign_up_page.dropdown_list)
            # for element in dropdown_list:
            #     if "United Kingdom +44" in element.text:
            #         element.click()
            mobile_num = self.element_to_be_clickable(sign_up_page.mobile_number)
            mobile_num.send_keys(usr_data[1])
            password = self.wait.until(expected_conditions.element_to_be_clickable(sign_up_page.password))
            password.send_keys(usr_data[2])
            pass_text = password.get_attribute("value")
            assert len(pass_text) >= 6
            Verify_Button = self.element_to_be_clickable(sign_up_page.verify_mobile_number)
            Verify_Button.click()

        except Exception as error:
            self.handle_exceptions(log, error, "SignUpForm_Validation")

    def test_solve_puzzle(self):
        verify_page = verification_Page(self.driver)
        self.driver.implicitly_wait(5)
        try:
            iFrame = self.check_visibility_of_element(verify_page.frame)
            self.driver.switch_to.frame(iFrame)
            print("Frame 1", iFrame)
            div1_tag = self.check_visibility_of_element(verify_page.div1_tag)
            iFrame2 = div1_tag.find_element(By.TAG_NAME, "iframe")

            self.driver.switch_to.frame(iFrame2)
            print("Frame 2", iFrame2)

            div2_tag = self.check_visibility_of_element(verify_page.div2_tag)
            iFrame3 = div2_tag.find_element(By.TAG_NAME, "iframe")
            self.driver.switch_to.frame(iFrame3)
            print("Frame 3", iFrame3)

            div3_tag = self.check_visibility_of_element(verify_page.div3_tag)
            iFrame4 = div3_tag.find_element(By.TAG_NAME, "iframe")
            self.driver.switch_to.frame(iFrame4)
            print("Frame 4", iFrame4)

            div_btn = self.check_visibility_of_element(verify_page.div_btn)
            puzzle_btn = div_btn.find_element(By.XPATH, "//button[text()='Start Puzzle']")
            puzzle_btn.click()
        except Exception as err:
            print("Error in iFrame", err)

    def handle_exceptions(self, log, error, screenshot_name):
        error_message = f"Error occurred: {str(error)}"
        log.critical(str(error_message))
        screenshot = "C:\\Users\\rawat\\PycharmProjects\\Amazon\\Amazon\\Reports\\{screenshot_name}.png"
        self.driver.get_screenshot_as_file(screenshot)

    if __name__ == "__main__":
        pytest.main()
