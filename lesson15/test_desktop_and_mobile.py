import pytest
from selene import browser
from conftest import set_browser_size
from site_classes import Site

site = Site()


# Тесты для десктопной версии
@pytest.mark.parametrize("window_size", [(1920, 1080), (375, 812)], indirect=True)
def test_sign_in_desktop_with_indirect(set_browser_size):
    if set_browser_size == 'desktop':
        site.desktop.sing_in()
    else:
        pytest.skip("Пропуск теста для мобильного разрешения")


# Тест для мобильной версии
@pytest.mark.parametrize("window_size", [(1920, 1080), (375, 812)], indirect=True)
def test_sign_in_mobile_with_indirect(set_browser_size):
    if set_browser_size == 'mobile':
        site.mobile.sing_in()
    else:
        pytest.skip("Пропуск теста для мобильного разрешения")


# Тесты для десктопной версии
def test_sign_in_desktop(set_browser_size_desktop):
    if browser.config.window_width > 900:
        site.desktop.sing_in()
    else:
        pytest.skip("Пропуск теста для мобильного разрешения")


# Тест для мобильной версии
def test_sign_in_mobile(set_browser_size_mobile):
    if browser.config.window_width <= 900:
        site.mobile.sing_in()
    else:
        pytest.skip("Пропуск теста для мобильного разрешения")
