from selenium.webdriver.common.by import By


class homePage:

    def __init__(self, driver):
        self.driver = driver

    Search_Product = (By.ID, "twotabsearchtextbox")
    Result_msg = (By.XPATH, "//div[@class = 'a-section a-spacing-small a-spacing-top-small']")
    Account_lists = (By.ID, "nav-link-accountList")
    links = (By.TAG_NAME, "a")
    fresh = (By.ID, "nav-link-groceries")
    fresh_groceries_btn = (By.XPATH, "//img[@alt = 'Amazon Fresh']")
    login_btn = (By.CLASS_NAME, "nav-action-signin-button")
