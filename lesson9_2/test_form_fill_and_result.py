from students import daria
from form_classes import Application


def test_fill_form():
    app = Application(daria)

    app.registration.open_reg_page().fill_registration_page(daria).submit_form()
    app.result.check_result(daria)
