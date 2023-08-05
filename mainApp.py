from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('./main.kv')

background_color = (253/255, 240/255, 213/255, 1)
text_color = (240/255, 240/255, 240/255, 1)
main_color_1 =  (0, 18.8/255, 28.6/255, 1 )
main_color_2 = (193/255, 18/255, 31/255, 1)


class WelcomePage(Widget):
    page_color = main_color_1
    pass

class RootClass(Widget):
    background_color = (253/255, 240/255, 213/255, 1)
    text_color = (240/255, 240/255, 240/255, 1)
    main_color_1 =  (0, 18.8/255, 28.6/255, 1 )
    pass

class LoginButton(Button):
    text_color = text_color
    background_color = main_color_1
    button_color = main_color_2

    def press(self, widget, *args):
        animate = Animation(opacity=0, duration=0.7)
        animate.start(widget)
        animate.start(args[0])
    pass

class ScreenTwo(Screen):
    pass

class ScreenOne(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(ScreenOne())
screen_manager.add_widget(ScreenTwo(name="screen_two"))

class MainWindow(App):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    MainWindow().run()
