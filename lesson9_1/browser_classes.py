import os

from selene import browser, have


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.user_number = browser.element('#userNumber')
        self.subjects_input = browser.element('#subjectsInput')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.result = browser.element('.modal-content').element('table').all('tr').all('td')

    def open_registration_form(self):
        browser.open('/automation-practice-form')
        return self

    def choose_gender(self):
        browser.element('#genterWrapper').element('input[value="Female"]').element('..').click()
        return self

    def choose_hobbies(self):
        browser.element('#hobbies-checkbox-1').element('..').click()
        browser.element('#hobbies-checkbox-3').element('..').click()
        return self

    def upload_pic(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('img.png'))
        return self

    def fill_birth_date(self, day: int, month: int, year: int):
        browser.element('#dateOfBirthInput').click()
        browser.element(
            f'.react-datepicker__month-select option[value="{month - 1}"]').click()
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day'
                        f'.react-datepicker__day--{day:03d}').click()
        return self

    def result_bill(self):
        browser.element('#submit').click()
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_user_email(self, value):
        self.user_email.type(value)
        return self

    def fill_user_number(self, value):
        self.user_number.type(value)
        return self

    def fill_subjects_input(self, value):
        self.subjects_input.type(value).press_tab()
        return self

    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    def fill_state(self, value):
        self.state.type(value).press_tab()
        return self

    def fill_city(self, value):
        self.city.type(value).press_tab()
        return self

    def check_result(self, fullname, email, gender, phone, bday, subject1, hobbies, img, addr, city_and_state):
        assert self.result.even.should(have.exact_texts(fullname,
                                                        email,
                                                        gender,
                                                        phone,
                                                        bday,
                                                        subject1,
                                                        hobbies,
                                                        img,
                                                        addr,
                                                        city_and_state))
        return self
