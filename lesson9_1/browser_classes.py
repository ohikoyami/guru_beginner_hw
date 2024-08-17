import os

from selene import browser, have


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.userEmail = browser.element('#userEmail')
        self.userNumber = browser.element('#userNumber')
        self.subjectsInput = browser.element('#subjectsInput')
        self.currentAddress = browser.element('#currentAddress')
        self.State = browser.element('#react-select-3-input')
        self.City = browser.element('#react-select-4-input')
        self.Result = browser.element('.modal-content').element('table').all('tr').all('td')

    def open_registration_form(self):
        browser.open('/automation-practice-form')
        return self

    def chooseGender(self):
        browser.element('#genterWrapper').element('input[value="Female"]').element('..').click()
        return self

    def chooseHobbies(self):
        browser.element('#hobbies-checkbox-1').element('..').click()
        browser.element('#hobbies-checkbox-3').element('..').click()
        return self

    def uploadPic(self):
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

    def resultBill(self):
        browser.element('#submit').click()
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_userEmail(self, value):
        self.userEmail.type(value)
        return self

    def fill_userNumber(self, value):
        self.userNumber.type(value)
        return self

    def fill_subjectsInput(self, value):
        self.subjectsInput.type(value).press_tab()
        return self

    def fill_currentAddress(self, value):
        self.currentAddress.type(value)
        return self

    def fill_State(self, value):
        self.State.type(value).press_tab()
        return self

    def fill_City(self, value):
        self.City.type(value).press_tab()
        return self

    def check_Result(self, fullname, email, gender, phone, bday, subject1, hobbies, img, addr, CityAndState):
        assert self.Result.even.should(have.exact_texts(fullname,
                                                 email,
                                                 gender,
                                                 phone,
                                                 bday,
                                                 subject1,
                                                 hobbies,
                                                 img,
                                                 addr,
                                                 CityAndState))
        return self