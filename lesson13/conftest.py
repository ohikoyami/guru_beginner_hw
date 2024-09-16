import pytest
from selene import browser


@pytest.fixture(autouse=True)
def manage_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10
    browser.maximize_window()

    yield browser

    browser.quit()
    print("Браузер закрыт фикстурой")