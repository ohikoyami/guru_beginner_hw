import os.path

from selene import browser, have

def fill_birth_date(day: int, month: int, year: int):
    browser.element('#dateOfBirthInput').click()
    browser.element(f'.react-datepicker__month-select option[value="{month - 1}"]').click() #месяцы идут от 0 до 11
    browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()

    # day:03d это добавление 0 перед числом в зависимости от его длины
    browser.element(f'.react-datepicker__day'
                    f'.react-datepicker__day--{day:03d}').click()

def test_fill_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Daria')
    browser.element('#lastName').type('Bilenko')
    browser.element('#userEmail').type('e.mail@dssl.ru')

    # выбор элемента с явным указанием гендера
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
    browser.element('#submit').click()

    ''' проверка корректных данных в итоговой форме:
    # Проверка осуществляется в четных ячейках таблицы (td) внутри модального окна (.modal-content)
    # Получаем элемент модального окна - browser.element('.modal-content')
    # Находим элемент таблицы внутри модального окна - element('table')
    # Получаем все строки таблицы - all('tr')
    # Получаем все ячейки таблицы внутри строк - all('td')
    # Отфильтровываем только четные ячейки - even
    # Проверяем, что текст в этих ячейках точно соответствует ожидаемому - should(have.exact_texts()'''

    assert browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
        'Daria Bilenko',
        'e.mail@dssl.ru',
        'Female',
        '9876541234',
        '09 April,2002',
        'Maths',
        'Sports, '
        'Music',
        'img.png',
        'st. Skobelevskaya',
        'Rajasthan Jaipur'))
