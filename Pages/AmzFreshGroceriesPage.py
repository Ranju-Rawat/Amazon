from selenium.webdriver.common.by import By


class FreshGroceries:

    def __init__(self, driver):
        self.driver = driver

    fresh_logo = (By.XPATH, "//img[@alt = 'Amazon Fresh Logo']")
    skip_location = (By.LINK_TEXT, "Skip")
    fruits_veg = (By.XPATH, "//img[@alt ='F&V']")
    all_fruits = (By.XPATH, "//img[@alt='All fruits']")
    pear_fruit = (By.CSS_SELECTOR, "div[data-index='18']")
