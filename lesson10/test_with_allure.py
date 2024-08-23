from selene import browser, have, by
import allure
from allure_commons.types import Severity, AttachmentType


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка названия Issue')
@allure.story('Тест без шагов и декоратора')
@allure.link('https://github.com', name='Testing')
def test_issue_title_with_only_selene():
    browser.open(browser.config.base_url)
    browser.element('.search-input-container').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').submit()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element('#issue_81_link').should(have.text('issue_to_test_allure_report'))


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка названия Issue')
@allure.story('Тест с шагами')
@allure.link('https://github.com', name='Testing')
def test_with_allure_steps():
    with allure.step('Открытие главной страницы GitHub'):
        browser.open(browser.config.base_url)

    with allure.step('Поиск репозитория eroshenkoam/allure-example'):
        browser.element('.search-input-container').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example').submit()

    with allure.step('Переход в репозиторий eroshenkoam/allure-example'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открытие вкладки Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверка названия Issues'):
        browser.element('#issue_81_link').should(have.text('issue_to_test_allure_report'))


@allure.step('Открытие главной страницы GitHub')
def open_github():
    browser.open(browser.config.base_url)


@allure.step('Поиск репозитория eroshenkoam/allure-example')
def search_repository(repository):
    browser.element('.search-input-container').click()
    browser.element('#query-builder-test').type(repository).submit()


@allure.step('Переход в репозиторий eroshenkoam/allure-example')
def open_repository(repository):
    browser.element(by.link_text(repository)).click()


@allure.step('Открытие вкладки Issues')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверка названия Issues')
def check_issue_title(issue_title):
    browser.element('#issue_81_link').should(have.text(issue_title))


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка названия Issue')
@allure.story('Тест с декоратором')
@allure.link('https://github.com', name='Testing')
def test_wint_allure_decorator():
    open_github()
    search_repository('eroshenkoam/allure-example')
    open_repository('eroshenkoam/allure-example')
    open_issues_tab()
    check_issue_title('issue_to_test_allure_report')
