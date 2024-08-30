import calendar
import os

from selene import browser, have


class Student:
    def __init__(self, name, lastname, email, phone, subject1, addr,
                 city, state, gender, bday_day, bday_month, bday_year, hobbies1, hobbies2, img):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.subject1 = subject1
        self.addr = addr
        self.city = city
        self.state = state

        self.gender = gender
        self.bday_day = bday_day
        self.bday_month = bday_month
        self.bday_year = bday_year
        self.hobbies1 = hobbies1
        self.hobbies2 = hobbies2
        self.img = img


class RegistrationPage:

    def __init__(self, student: Student):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.choose_gender = browser.element('#genterWrapper').element(f'input[value={student.gender}]').element('..')
        self.user_number = browser.element('#userNumber')
        self.subjects_input = browser.element('#subjectsInput')
        self.choose_hobbies1 = browser.element('#hobbies-checkbox-1').element('..')
        self.choose_hobbies3 = browser.element('#hobbies-checkbox-3').element('..')
        self.upload_pic = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.result_bill = browser.element('#submit')

    def open_reg_page(self):
        browser.open('/automation-practice-form')
        return self

    def fill_registration_page(self, student: Student):
        self.first_name.type(student.name)
        self.last_name.type(student.lastname)
        self.user_email.type(student.email)
        self.choose_gender.click()
        self.user_number.type(student.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element(
            f'.react-datepicker__month-select option[value="{student.bday_month - 1}"]').click()
        browser.element(f'.react-datepicker__year-select option[value="{student.bday_year}"]').click()
        browser.element(f'.react-datepicker__day'
                        f'.react-datepicker__day--{student.bday_day:03d}').click()
        self.subjects_input.type(student.subject1).press_tab()
        self.choose_hobbies1.click()
        self.choose_hobbies3.click()
        self.upload_pic.send_keys(os.path.abspath(student.img))
        self.current_address.type(student.addr)
        self.state.type(student.state).press_tab()
        self.city.type(student.city).press_tab()
        return self

    def submit_form(self):
        self.result_bill.click()
        return self


class ProfilePage:
    def __init__(self):
        self.result = browser.element('.modal-content').element('table').all('tr').all('td').even

    def check_result(self, student: Student):
        day = f'{student.bday_day:02d}'
        month = f'{calendar.month_name[student.bday_month]}'

        assert self.result.should(have.exact_texts(f'{student.name} {student.lastname}',
                                                   student.email,
                                                   student.gender,
                                                   student.phone,
                                                   f'{day} {month},{student.bday_year}',
                                                   student.subject1,
                                                   f'{student.hobbies1}, {student.hobbies2}',
                                                   student.img,
                                                   student.addr,
                                                   f'{student.state} {student.city}'))
        return self


class Application:
    def __init__(self, student: Student):
        self.registration = RegistrationPage(student)
        self.result = ProfilePage()
