import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def preSetup(request):
    headless_options = Options()
    headless_options.add_argument("headless")
    browserName = request.config.getoption("browser_name").lower()

    if "chrome" in browserName:
        driver_path = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=driver_path)
        driver.get("https://www.amazon.in/")
    elif "firefox" in browserName:
        option = Options()
        option.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        driver_path = Service("C:\\Users\\rawat\\Downloads\\geckodriver-v0.34.0-win32\\geckodriver.exe")
        driver = webdriver.Firefox(service=driver_path, options=option)
        driver.get("https://www.amazon.in/")
    elif "edge" in browserName:
        driver_path = Service("C:\\Users\\rawat\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=driver_path)
        driver.get("https://www.amazon.in/")
    else:
        print("Browser does not exist")

    # driver.get("https://www.amazon.in/")
    wait = WebDriverWait(driver, 5)
    request.cls.driver = driver
    request.cls.wait = wait
    yield driver
    time.sleep(5)
    driver.quit()

