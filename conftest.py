import pytest
from selene import browser


@pytest.fixture(autouse=True)
def manage_browser():

    browser.config.window_height = 900 #фикстура - высота окна браузера
    browser.config.window_width = 900 #фикстура - ширина окна браузера
    browser.config.base_url = 'https://google.com'  # фикстура - дефолт браузер
    browser.open('/ncr') #подтверждение cookie
    print("Браузер открыт фикстурой")

    yield

    browser.quit() #фикстура - закрытие браузера после прогона
    print("Браузер закрыт фикстурой")
