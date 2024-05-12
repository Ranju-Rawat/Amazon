from selenium.webdriver.common.by import By


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    sign_up_button = (By.XPATH, "//div/div/div/a[@class = 'nav-a']")
    verify_mobile_number = (By.ID, "continue")
    error_msgs = (By.CSS_SELECTOR, "div[class='a-alert-content']")
    user_name = (By.ID, "ap_customer_name")
    click_country_dropdown = (By.CSS_SELECTOR, "#auth-country-picker-container")
    dropdown_list = (By.CSS_SELECTOR, "ul li a")
    mobile_number = (By.ID, "ap_phone_number")
    password = (By.ID, "ap_password")
