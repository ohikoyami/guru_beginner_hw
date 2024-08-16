import os.path

from selene import browser, have

from lesson9_1.browser_classes import RegistrationPage


def test_fill_form():
    (RegistrationPage()
     .open_registration_form()
     .fill_first_name('Daria')
     .fill_last_name('Bilenko')
     .fill_userEmail('e.mail@dssl.ru')
     .chooseGender()
     .fill_userNumber('9876541234')
     .fill_subjectsInput('Math')
     .chooseHobbies()
     .uploadPic()
     .fill_currentAddress('st. Skobelevskaya')
     .fill_State('raja')
     .fill_City('jaip')
     .fill_birth_date(9, 4, 2002)
     .resultBill()
     .check_Result(
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
        'Rajasthan Jaipur')
     )
