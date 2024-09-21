from selene import be, browser


class Desktop:
    def __init__(self):
        self.sing_in_button = browser.element('.HeaderMenu-link--sign-up')

    def sing_in(self):
        self.sing_in_button.should(be.visible).click()
        return self


class Mobile:
    def __init__(self):
        self.sing_in_button = browser.element('.HeaderMenu-link')
        self.width = browser.config.window_width

    def sing_in(self):
        self.sing_in_button.should(be.visible).click()
        return self


class Site:
    def __init__(self):
        self.desktop = Desktop()
        self.mobile = Mobile()
