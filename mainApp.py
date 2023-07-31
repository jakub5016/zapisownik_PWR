from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.lang.builder import Builder

Builder.load_file('./main.kv')


class welcomePage(Widget):
    background_color = (253/255, 240/255, 213/255, 1)
    text_color = (240/255, 240/255, 240/255, 1)
    button_color = (0, 48/255, 73/255, 1)
    warning_color = (193/255, 18/255, 31/255, 1)

    def login_press(self, widget, *args):
        animate = Animation(opacity=0, duration=0.7)
        animate.start(widget)

class mainWindow(App):
    def build(self):
        return welcomePage()


if __name__ == '__main__':
    mainWindow().run()
