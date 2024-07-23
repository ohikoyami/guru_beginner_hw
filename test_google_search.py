import pytest
from selene import browser, be, have

def open_browser():
    browser.open('/ncr')  #подтверждение cookie


def test_search_1():
    open_browser()
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_2():
    open_browser()
    browser.element('[name="q"]').should(be.blank).type('gfffddkk;kajjjfgggdgCXSJ').press_enter()
    browser.element('[id="botstuff"]').should(have.text('did not match any documents.'))
