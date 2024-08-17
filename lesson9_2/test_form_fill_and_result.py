import os.path

from selene import browser, have

from form_classes import RegistrationPage
from form_classes import CheckResultRegistrationPage
from form_classes import Student


def test_fill_form():
    daria = Student('Daria',
                    'Bilenko',
                    'e.mail@dssl.ru',
                    '9876541234',
                    'Maths',
                    'st. Skobelevskaya',
                    'Jaipur',
                    'Rajasthan',
                    'Female',
                    9,
                    4,
                    2002,
                    'Sports',
                    'Music',
                    'img.png'
                    )

    registration_page = RegistrationPage(daria)
    registration_result = CheckResultRegistrationPage()

    registration_page.open_reg_page()
    registration_page.fill_registration_page(daria)
    registration_page.fill_birth_date(daria)
    registration_page.submit_form()
    registration_result.check_Result(daria)
