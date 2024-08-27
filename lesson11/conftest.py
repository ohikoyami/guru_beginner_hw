import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

import subprocess


def get_chromedriver_version():
    result = subprocess.run(['chromedriver', '--version'], capture_output=True, text=True)
    return result.stdout.strip()


@pytest.fixture(autouse=True)
def manage_browser():
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
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'

    chromedriver_path = '/lesson11/chromedriver.exe'
    options = webdriver.ChromeOptions()

    capabilities = driver.capabilities
    chromedriver_version = capabilities.get('chrome')  # Версия браузера Chrome

    print(f'Chromedriver version: {capabilities.get("chrome", {}).get("version")}')
    print(f'Browser version: {capabilities.get("browserVersion")}')

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
    print("Браузер закрыт фикстурой")
