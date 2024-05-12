from selenium.webdriver.common.by import By


class verification_Page:
    def __init__(self, driver):
        self.driver = driver

    entr_otp = (By.ID, "auth-pv-enter-code")
    otp_submit_btn = (By.ID, "a-autoid-0")
    error_msg = (By.CSS_SELECTOR, "span[class='a-list-item']")
    frame = (By.ID, "cvf-aamation-challenge-iframe")
    div1_tag = (By.ID, "aacb-arkose-elements")
    frame2 = (By.CLASS_NAME, "aacb-captcha-iframe")
    div2_tag = (By.ID, "arkose")
    div3_tag = (By.ID, "FunCaptcha")
    div_btn = (By.ID, "root")
