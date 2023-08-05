from kivy.uix.widget import Widget
from colors import *

class LoginPage(Widget):
    background_color = background_color
    page_color = main_color_1
    text_color = text_color

    def on_text_validate(self, text_got):
        print(text_got)
    pass
