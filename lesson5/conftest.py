import pytest
from selene import browser


@pytest.fixture(autouse=True)
def manage_browser():
    browser.config.base_url = 'https://demoqa.com'  # фикстура - дефолт браузер
    browser.config.timeout = 2.0
    browser.open('/automation-practice-form') #подтверждение cookie + открытие браузера
    print("Браузер открыт фикстурой")

    yield

    browser.quit() #фикстура - закрытие браузера после прогона
    print("Браузер закрыт фикстурой")
