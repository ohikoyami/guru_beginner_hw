import allure
import allure_commons
import pytest
import requests
from appium.options.android import UiAutomator2Options
from selene import browser, support

import project_config

@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        'platformName': 'android',
        'platformVersion': '9.0',
        'deviceName': 'Google Pixel 3',

        # Set URL of the application under test
        'app': 'bs://sample.app',

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # Set your access credentials
            'userName': project_config.config.userName,
            'accessKey': project_config.config.accessKey
        }
    })

    browser.config.driver_remote_url = project_config.config.remote_url
    browser.config.driver_options = options
    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )
    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML
    )

    session_id = browser.driver.session_id

    browser.quit()

    response = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(project_config.config.userName, project_config.config.accessKey),
    ).json()

    video_url = response['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
