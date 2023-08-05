from kivy.uix.widget import Widget
from .colors import *
from selenium_code.login import login_edukacja_cl
import threading

class LoginPage(Widget):
    background_color = background_color
    page_color = main_color_1
    text_color = text_color
    username_got = ""
    password_got = ""
    def on_press(self):
        print(self.username_got, self.password_got)
        thread_to_login = threading.Thread(target=login_edukacja_cl, args=(self.username_got, self.password_got))
        thread_to_login.start()
    pass
