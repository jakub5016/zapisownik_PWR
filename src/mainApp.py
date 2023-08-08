from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import FadeTransition
from kivy_py.loginApp import LoginPage
from kivy_py.colors import *
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.label import Label

Window.minimum_width, Window.minimum_height = (700, 500)


class WelcomePage(Widget):
    background_color = background_color
    text_color = text_color
    main_color_1 =  main_color_1


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        with self.canvas:
            Color(*self.main_color_1)
            RoundedRectangle(pos=(Window.center[0]/2, Window.center[1]/2), size=(Window.width/2, Window.height/2), radius=[60, 60, 60, 60])
        label = Label(font_size=Window.width/28, center_x=Window.width / 2, center_y=Window.height * 0.55, text="Witaj w zapisowniku!", font_name="../fonts/Roboto-Black.ttf")
        self.add_widget(label)
        button = LoginButton(center_x=Window.width / 2, center_y=Window.height * 0.4)
        self.add_widget(button)


class LoginButton(Button):
    text_color = text_color
    background_color = main_color_1
    button_color = main_color_2
    background_normal = './graphics/transparent_background.png'
    background_down = './graphics/transparent_background.png'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(*self.button_color)
            RoundedRectangle(radius=[60, 60, 60, 60], size=self.size, pos=self.pos)
        label = Label(text="Zaloguj się", center_x=self.center_x, center_y=self.center_y, font_name="../fonts/Roboto-Black.ttf")
        self.add_widget(label)
        self.bind(on_press=self.on_button_press)

    def on_button_press(self, instance):
        self.parent.parent.manager.transition.duration = 0.7
        self.parent.parent.manager.transition.duration
        self.parent.parent.manager.current = "screen_two"

    def press(self):
        animate =Animation(size=(200,200), duration=0.7)
        animate.start(self)
        animate.start(self.parent)

    pass

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
