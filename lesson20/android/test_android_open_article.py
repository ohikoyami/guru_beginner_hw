import pytest
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_open():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Selene')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than_or_equal(0))
        results.first.should(have.text('Selene')).click()
