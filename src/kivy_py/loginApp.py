from kivy.uix.widget import Widget
from .colors import *
from selenium_code.login import login_edukacja_cl

class LoginPage(Widget):
    background_color = background_color
    page_color = main_color_1
    text_color = text_color
    username_got = ""
    password_got = ""
    def on_press(self):
        print(self.username_got, self.password_got)
        login_edukacja_cl(username=self.username_got, password=self.password_got)
    pass
