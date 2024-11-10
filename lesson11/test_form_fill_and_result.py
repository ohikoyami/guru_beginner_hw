import os.path
from selene import browser, have
import allure
from allure_commons.types import Severity


def fill_birth_date(day: int, month: int, year: int):
    browser.element('#dateOfBirthInput').click()
    browser.element(f'.react-datepicker__month-select option[value="{month - 1}"]').click()  #месяцы идут от 0 до 11
    browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()

    # day:03d это добавление 0 перед числом в зависимости от его длины
    browser.element(f'.react-datepicker__day'
                    f'.react-datepicker__day--{day:03d}').click()


@allure.step('Открытие формы для заполнения')
def open_form():
    browser.open('/automation-practice-form')


@allure.step('Заполнение формы')
def fill_form():
    browser.element('#firstName').type('Daria')
    browser.element('#lastName').type('Bilenko')
    browser.element('#userEmail').type('e.mail@dssl.ru')
    browser.element('#genterWrapper').element('input[value="Female"]').element('..').click()
    browser.element('#userNumber').type('9876541234')
    fill_birth_date(9, 4, 2002)
    browser.element('#subjectsInput').type('Math').press_tab()
    browser.element('#hobbies-checkbox-1').element('..').click()
    browser.element('#hobbies-checkbox-3').element('..').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img.png'))
    browser.element('#currentAddress').type('st. Skobelevskaya')
    browser.element('#react-select-3-input').type('raja').press_tab()
    browser.element('#react-select-4-input').type('jaip').press_tab()


@allure.step('Подтверждение данных в форме')
def submit_form():
    browser.element('#submit').click()


@allure.step('Проверка результатов заполнения формы')
def check_result():
    assert browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
        'Daria Bilenko',
        'e.mail@dssl.ru',
        'Female',
        '9876541234',
        '09 April,2002',
        'Maths',
        'Sports, '
        'Music',
        'test_results.png',
        'st. Skobelevskaya',
        'Rajasthan Jaipur'))


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка заполнения формы')
@allure.story('Тест формы')
def test_fill_form():
    open_form()
    fill_form()
    submit_form()
    check_result()
