import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach
from dotenv import load_dotenv


@pytest.fixture(autouse=True)
def manage_browser():
    load_dotenv()
    selenoid_user = os.getenv('SELENOID_USER')
    selenoid_password = os.getenv('SELENOID_PASSWORD')

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "126.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_user}:{selenoid_password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10
    driver.maximize_window()

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_source(browser)
    attach.add_video(browser)

    browser.quit()
    print("Браузер закрыт фикстурой")
