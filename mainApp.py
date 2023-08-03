from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.button import Button
Builder.load_file('./main.kv')

class WelcomePage(Widget):
    pass

class RootClass(Widget):
    pass

class LoginButton(Button):
    is_presed = False
    pass

class MainWindow(App):
    def build(self):
        return RootClass()


if __name__ == '__main__':
    MainWindow().run()
