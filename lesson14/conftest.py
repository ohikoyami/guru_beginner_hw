import os
import pytest
from selene import browser, command
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
    browser.config.base_url = 'https://krispykreme-moskva.ru'
    browser.config.timeout = 10
    browser.open('/')
    driver.maximize_window()

    yield browser

    browser.quit()
    print("Браузер закрыт фикстурой")


@pytest.fixture(autouse=True)
def attach_result(request, manage_browser):
    yield
    attach.add_screenshot(manage_browser)
    attach.add_logs(manage_browser)
    attach.add_source(manage_browser)
    attach.add_video(manage_browser)
