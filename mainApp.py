from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.lang.builder import Builder

Builder.load_file('./main.kv')

class rootClass(Widget):
    background_color = (253/255, 240/255, 213/255, 1)
    pass

class welcomePage(Widget):
    pass

class mainWindow(App):
    def build(self):
        return rootClass()


if __name__ == '__main__':
    mainWindow().run()
