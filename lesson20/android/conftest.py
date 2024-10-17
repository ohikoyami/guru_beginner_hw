import allure
import allure_commons
import pytest
from appium import webdriver
from selene import browser, support
from utils.allure_attachs import attach_screenshot, attach_screen_xml_dump, attach_bstack_video
import project


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            project.config.url,
            options=project.config.to_driver_options()
        )
    browser.config.timeout = project.config.timeout

    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield

    attach_screenshot()

    attach_screen_xml_dump()

    session_id = browser.driver.session_id

    browser.quit()

    if project.config.context == 'bstack':
        attach_bstack_video(session_id)
