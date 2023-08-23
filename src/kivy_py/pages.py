from kivy_py.colors import *
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy_py.rounded_widgets import LoginButton
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy_py.time_converter import time_converter
from kivy_py.rounded_widgets import RoundedDay

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


class MainPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first_day_x = 250
        self.day_iterator= 120 # Size in pixels between first and second day in week (in x-axis)

        self.add_widget(ClassDate(text="AAA", day=1, time = "07:30"))
        self.add_widget(ClassDate(text="AAA", day=0, time = "21:15"))
    pass


class ClassDate(Button):
    def __init__(self, day, time, type=None, **kwargs):
        super().__init__(**kwargs)

        self.first_day_x = Window.width*2/7 + Window.width/7/2 # First day coordinates, this is a center so i have to add half of the size 
        self.day_iterator= Window.width/7 # Size in pixels between first and second day in week (in x-axis)

        self.size=(Window.width/7, time_converter("01:30")) # Size of Button fixed
        self.size_hint= (None, None)

        self.center_x = self.first_day_x + day * Window.width/7 # Define day as Monday = 0, Tuesday=1 ... etc.

        self.center_y = time_converter(time)
        print(time_converter("01:30"))

        if type != None:
            self.type = type



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
        with self.canvas:
            Color(*main_color_1)
            RoundedRectangle(radius=[60, 60, 60, 60], size=self.size, pos=self.pos)


        self.add_widget(RoundedDay(text="Poniedziałek"))
        self.add_widget(RoundedDay(text="Wtorek"))
        self.add_widget(RoundedDay(text="Środa"))
        self.add_widget(RoundedDay(text="Czwartek"))
        self.add_widget(RoundedDay(text="Piątek"))

class HourInfo(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(size=self.size, pos = self.pos))
        self.add_widget(Label(text="07:30", center_y = self.center_y +Window.width/4.5))