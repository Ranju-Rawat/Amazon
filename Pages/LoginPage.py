from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_mobile = (By.ID, "ap_email")
    continue_btn = (By.ID, "continue")
    password = (By.ID, "ap_password")
    sign_in = (By.ID, "signInSubmit")