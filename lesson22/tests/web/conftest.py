import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
from allure_commons.types import AttachmentType


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

    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')

    browser.quit()
    print("Браузер закрыт фикстурой")
