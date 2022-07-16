import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.binary_location = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    # List with all option https://peter.sh/experiments/chromium-command-line-switches/
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1600,900')
    # options.add_argument("--disable-notifications")
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    if driver.find_element(By.ID, 'tinybox'):
        close_link = driver.find_element(By.ID, 'closeButton')
        if close_link:
            close_link.click()
    yield driver
    driver.quit()
