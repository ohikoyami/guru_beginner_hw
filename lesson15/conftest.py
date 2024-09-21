import pytest
from selene import browser


# Фикстура для установки размеров окна
@pytest.fixture(params=[(1920, 1080), (375, 812)], ids=["desktop", "mobile"])
def window_size(request):
    return request.param


@pytest.fixture(params=[(1920, 1080), (1120, 950), (375, 812)], ids=["desktop", "desktop", "mobile"])
def window_size_desktop(request):
    return request.param


@pytest.fixture(params=[(766, 766), (500, 860), (1920, 1080)], ids=["mobile", "mobile", "desktop"])
def window_size_mobile(request):
    return request.param


# Фикстура для конфигурации браузера под разные размеры экрана
@pytest.fixture
def set_browser_size(window_size):
    browser.config.window_width, browser.config.window_height = window_size
    browser.open('https://github.com')
    if browser.config.window_width > 900:
        yield 'desktop'
    else:
        yield 'mobile'
    browser.quit()


# Фикстура для установки размеров окна на ПК
@pytest.fixture
def set_browser_size_desktop(window_size_desktop):
    browser.config.window_width, browser.config.window_height = window_size_desktop
    browser.open('https://github.com')
    yield
    browser.quit()


# Фикстура для установки размеров окна на мобильные
@pytest.fixture
def set_browser_size_mobile(window_size_mobile):
    browser.config.window_width, browser.config.window_height = window_size_mobile
    browser.open('https://github.com')
    yield
    browser.quit()
