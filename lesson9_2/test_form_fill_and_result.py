from students import daria
from form_classes import Application


def test_fill_form():
    app = Application(daria)

    app.registration.open().fill(daria).submit()
    app.result.check_form(daria)
