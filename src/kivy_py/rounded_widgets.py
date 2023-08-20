from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy_py.colors import *


class RoundedButton(Button):
    def __init__(self, button_color=(1, 1, 1, 1), background_color= (1,1,1,1), **kwargs):
        super().__init__(**kwargs)
        self.background_normal = './graphics/transparent_background.png'
        self.background_down = './graphics/transparent_background.png'
        self.background_color = background_color
        with self.canvas:
            Color(*button_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[30, 30, 30, 30])

        self.animation = Animation(opacity=0, duration = 1)
        self.label = Label(text="Zaloguj się!", center_x=self.center_x, center_y=self.center_y, font_name="../fonts/Roboto-Black.ttf" )
        self.add_widget(self.label)

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

class RoundedDay(Button):
    background_color = main_color_2
    background_normal = './graphics/transparent_background.png'
    background_down = './graphics/transparent_background.png'

