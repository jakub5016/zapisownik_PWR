from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import FadeTransition
from kivy_py.loginApp import LoginPage
from kivy_py.colors import *
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.label import Label
from kivy_py.rounded_widgets import LoginButton
from kivy_py.pages import WelcomePage


Window.minimum_width, Window.minimum_height = (700, 500)


class ScreenTwo(Screen):
    background_color = background_color

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (Window.width, Window.height)
        with self.canvas:
            Color(*background_color) # To unpack colors
            self.rect = RoundedRectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        login_page = LoginPage()
        self.add_widget(login_page)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class ScreenOne(Screen):
    background_color = background_color

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (Window.width, Window.height)
        with self.canvas:
            Color(*background_color) # To unpack colors
            self.rect = RoundedRectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        welcome_page = WelcomePage()
        self.add_widget(welcome_page)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    pass

class MainWindow(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        screen_one = ScreenOne(name='screen_one')
        screen_two = ScreenTwo(name='screen_two')
        sm.add_widget(screen_one)
        sm.add_widget(screen_two)
        return sm

if __name__ == '__main__':
    MainWindow().run()
