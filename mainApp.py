from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('./main.kv')

class background(Widget):
    pass

class welcomePage(Widget):
    background_color = (253/255, 240/255, 213/255, 1)
    text_color = (240/255, 240/255, 240/255, 1)
    button_color = (0, 48/255, 73/255, 1)
    warning_color = (193/255, 18/255, 31/255, 1)
    background = background()
    pass

class mainWindow(App):
    def build(self):
        return welcomePage()


if __name__ == '__main__':
    mainWindow().run()
