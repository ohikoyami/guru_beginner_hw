import os.path

from selene import browser, have


def test_fill_form():
    browser.element('#firstName').type('Daria')
    browser.element('#lastName').type('Bilenko')
    browser.element('#userEmail').type('e.mail@dssl.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').type('9876541234')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="3"]').click()
    browser.element('.react-datepicker__year-select option[value="2002"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--009').click()
    browser.element('#subjectsInput').type('M').press_tab()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img.png'))
    browser.element('#currentAddress').type('st. Skobelevskaya')
    browser.element('#react-select-3-input').type('raja').press_tab()
    browser.element('#react-select-4-input').type('jaip').press_tab()
    browser.element('#submit').click()
    assert browser.element(".modal-content").element('table').all('tr').all('td').even.should(have.exact_texts(
        'Daria Bilenko',
        'e.mail@dssl.ru',
        'Other',
        '9876541234',
        '09 April,2002',
        'Maths',
        'Sports, '
        'Reading, '
        'Music',
        'img.png',
        'st. Skobelevskaya',
        'Rajasthan Jaipur'))
