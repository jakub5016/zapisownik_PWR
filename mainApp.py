from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('./main.kv')

class background(Widget):
    pass

class welcomePage(Widget):
    background = background()
    pass

class RoundedButton(Widget):
    text_included = ""
    pass

class mainWindow(App):
    def build(self):
        return welcomePage()


if __name__ == '__main__':
    mainWindow().run()
