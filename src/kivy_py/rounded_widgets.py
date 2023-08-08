from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

class RoundedButton(Button):
     def __init__(self, button_color=(1, 1, 1, 1), background_color= (1,1,1,1), **kwargs):
        super().__init__(**kwargs)
        self.background_normal = './graphics/transparent_background.png'
        self.background_down = './graphics/transparent_background.png'
        self.background_color = background_color
        with self.canvas:
            Color(*button_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[30, 30, 30, 30])

