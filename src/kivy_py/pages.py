from kivy_py.colors import *
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy_py.rounded_widgets import LoginButton
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

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


class MainPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for _ in range(5):
            self.add_widget(Button(text="AAA"))
    pass


class Day(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="AAA"))

class Dashboard(BoxLayout):
    orientation = 'horizontal'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Button(text="Profile"))
        self.add_widget(Button(text="Logout"))

class DaysInfo(BoxLayout):
    orientation = 'horizontal'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Button(text="Poniedziałek"))
        self.add_widget(Button(text="Wtorek"))
        self.add_widget(Button(text="Środa"))
        self.add_widget(Button(text="Czwartek"))
        self.add_widget(Button(text="Piątek"))
