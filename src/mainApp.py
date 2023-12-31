from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import FadeTransition
from kivy_py.loginApp import LoginPage
from kivy_py.colors import *
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy_py.pages import WelcomePage, MainPage, Dashboard, DaysInfo, HourInfo
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

# Fixed Window Size
Window.size = (800, 600)
# Window.borderless = True

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

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(*main_color_1)
            self.rect = RoundedRectangle(pos=self.pos, size=(4000, 4000))


        self.layout = GridLayout(cols=2, rows=2)


        dashboard = Dashboard(size_hint_x=None, width=Window.width * 2 / 7, size_hint_y=None, height=Window.height / 4)
        days_info = DaysInfo(size_hint_y=None, height=Window.height / 4)
        hour_info = HourInfo(size_hint_x=None, width=Window.width * 2 / 7)
        
        main_page = MainPage(size_hint=(None, None), size=(Window.width * 3 / 7, Window.height / 2))  # Set explicit size

        self.layout.add_widget(dashboard)
        self.layout.add_widget(days_info)
        self.layout.add_widget(hour_info)
        self.layout.add_widget(main_page)

        self.add_widget(self.layout)
        


class MainWindow(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        screen_one = ScreenOne(name='screen_one')
        screen_two = ScreenTwo(name='screen_two')
        main_screen = MainScreen(name="main_screen")
        # sm.add_widget(screen_one)
        # sm.add_widget(screen_two)
        # sm.add_widget(main_screen)
        sm.add_widget(main_screen)
        sm.add_widget(screen_two)
        sm.add_widget(screen_one)
        return sm

if __name__ == '__main__':
    MainWindow().run()
