import os.path

from selene import browser, have

from lesson9_1.browser_classes import RegistrationPage


def test_fill_form():
    (RegistrationPage()
     .open_registration_form()
     .fill_first_name('Daria')
     .fill_last_name('Bilenko')
     .fill_user_email('e.mail@dssl.ru')
     .choose_gender()
     .fill_user_number('9876541234')
     .fill_subjects_input('Math')
     .choose_hobbies()
     .upload_pic()
     .fill_current_address('st. Skobelevskaya')
     .fill_state('raja')
     .fill_city('jaip')
     .fill_birth_date(9, 4, 2002)
     .result_bill()
     .check_result(
        'Daria Bilenko',
        'e.mail@dssl.ru',
        'Female',
        '9876541234',
        '09 April,2002',
        'Maths',
        'Sports, Music',
        'img.png',
        'st. Skobelevskaya',
        'Rajasthan Jaipur')
     )
