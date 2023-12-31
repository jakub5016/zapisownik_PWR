from kivy.uix.widget import Widget
from .colors import *
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy_py.rounded_widgets import RoundedButton
from kivy.uix.image import Image

class LoginPage(Widget):
    background_color = background_color
    page_color = main_color_1
    button_color = main_color_2
    text_color = text_color
    username_got = ""
    password_got = ""
    logged = False
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.pos = (Window.center[0]/2, Window.center[1]/2 - (0.22*Window.center[1]) )
        self.width = Window.width/2
        self.height = Window.height/2 + (0.22*Window.height)
        with self.canvas:
            Color(*self.page_color)
            self.page = RoundedRectangle(pos=self.pos, size=self.size, radius=[60, 60, 60, 60])

        # Label
        label1 = Label(font_size=self.width/10, center_x=self.center_x, center_y=self.center_y + (0.5 * self.center_y), text="Logowanie", font_name="../fonts/Roboto-Black.ttf")
        self.add_widget(label1)

        # Username
        label2 = Label(font_size=self.width/16, center_x=self.center_x, center_y=self.center_y + (0.3 * self.center_y), text="Nazwa użytkownika", font_name="../fonts/Roboto-Black.ttf")
        self.add_widget(label2)
        self.username_input = TextInput(multiline=False, font_size=self.width/16, center_x=self.center_x - 100 , center_y=self.center_y + (0.2 * self.center_y), height=self.width/8, width=300, on_enter=self.on_button_press)
        self.add_widget(self.username_input)

        # Password
        label3 = Label(font_size=self.width/16, center_x=self.center_x, center_y=self.center_y - (0.1 * self.center_y), text="Hasło", font_name="../fonts/Roboto-Black.ttf")
        self.add_widget(label3)
        self.password_input = TextInput(multiline=False, font_size=self.width/16, center_x=self.center_x - 100 , center_y=self.center_y - (0.2 * self.center_y), height=self.width/8, width=300, password=True, on_enter=self.on_button_press)
        self.add_widget(self.password_input)

        # Button
        self.button = RoundedButton(center_x=self.center_x-50, center_y=self.center_y - (0.6 * self.center_y) +35, size=(200, 70), on_press=self.on_button_press,button_color=self.button_color, background_color = self.page_color)
        self.add_widget(self.button)

        # Gif after press
        self.gif_image = Image(center_x=self.center_x+20, center_y=self.center_y - (0.6 * self.center_y) +35, size=(70, 70),source='../graphics/Loading.gif', anim_delay = -1, opacity=0, anim_loop=300)
        self.add_widget(self.gif_image)

        # Warining
        self.label4 = Label(text = "ZŁE HASŁO LUB NAZWA UŻYTKOWNIKA", font_size=self.width/32, font_name="../fonts/Roboto-Black.ttf", center_x=self.center_x-50, center_y=self.center_y - (0.6 * self.center_y) +60, size=(200, 70), opacity=0, color=(1,0,0,1))
        self.add_widget(self.label4)

    def on_button_press(self, instance):
        self.username_got = self.username_input.text
        self.password_got = self.password_input.text
        self.on_press()


    def login_usos(self):
        login_url = "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex&locale=pl"

        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # headless - web browser without graphic interface
        driver = webdriver.Firefox(options=options)

        try:
            # Get site after login
            print("LOGGING IN")
            driver.get(login_url)

            username_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
            password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
            login_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[4]/form/div[2]/button[1]")

            username_input.send_keys(self.username_got)
            password_input.send_keys(self.password_got)
            login_button.click()

            driver.implicitly_wait(10)
            print("LOGIN COMPLETE")

            try:
                driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/span")
            except:
                self.logged = True

            with open("output.html", "w", encoding="utf-8") as file:
                file.write(driver.page_source)

        finally:
            driver.quit()

        Clock.schedule_once(lambda dt: self.button.animation.stop(self), 0)
        if self.logged == True:
            Animation(size= (Window.width, Window.height)).start(self.page)
            Clock.schedule_once(self.change_to_screen_one, 0)
        else:
            # Animation to create place for error and place it
            Animation(opacity = 0, duration=1).start(self.gif_image) # Stop loading
            Animation(opacity = 1, duration=1).start(self.label4) # Show error
            Animation(size=((Window.width/2), Window.height/2 + (0.22*Window.height)+50),pos=(self.pos[0], self.pos[1]-35), duration=1).start(self.page) # Resize page
            Animation(opacity = 1, pos=(self.pos[0]+100, self.pos[1]-15), duration =1).start(self.button)
            Animation(pos=self.button.pos).start(self.button.rect)
            Animation(center_y=self.button.center_y-35).start(self.button.label)

    def change_to_screen_one(self, dt):
        self.parent.parent.current = 'main_screen'  # Zmiana ekranu na "screen_one"


    def on_press_animation(self):
        show_loading = Animation(opacity = 1, duration = 1)
        show_loading.start(self.gif_image)
        self.gif_image.anim_delay = 0.25
        self.gif_image.anim = True
        self.button.animation.start(self.button)

    def on_press(self):
        print(self.username_got, self.password_got)
        self.on_press_animation()
        thread_to_login = threading.Thread(target=self.login_usos, args=())
        thread_to_login.start()

