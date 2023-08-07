from kivy.uix.widget import Widget
from .colors import *
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from kivy.animation import Animation
from kivy.clock import Clock


class LoginPage(Widget):
    background_color = background_color
    page_color = main_color_1
    text_color = text_color
    username_got = ""
    password_got = ""
    logged = False
    animation = Animation(opacity=1, duration=30)

    def login_edukacja_cl(self):
        login_url = "https://edukacja.pwr.wroc.pl/EdukacjaWeb/studia.do"

        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # headless - web browser without graphic interface
        driver = webdriver.Firefox(options=options)

        try:
            # Get site after login
            print("LOGGING IN")
            driver.get(login_url)

            username_input = driver.find_element(By.NAME, "login")
            password_input = driver.find_element(By.NAME, "password")
            login_button = driver.find_element(By.CLASS_NAME, "BUTTON_ZALOGUJ")

            username_input.send_keys(self.username_got)
            password_input.send_keys(self.password_got)
            login_button.click()

            driver.implicitly_wait(10)
            print("LOGIN COMPLETE")
            self.logged = True

            # Go to zapisy
            # print("GOING TO \"ZAPISY\"")
            # driver.find_element(By.XPATH, "//*[contains(text(), 'Zapisy')]").click()

            # driver.implicitly_wait(10)

            with open("output.html", "w", encoding="utf-8") as file:
                file.write(driver.page_source)

            # print("Zawartość strony została zapisana do pliku 'output.html'.")

        finally:
            driver.quit()

        Clock.schedule_once(lambda dt: self.animation.stop(self), 0)

    def on_press_animation(self):
        self.animation.start(self)

    def on_press(self):
        print(self.username_got, self.password_got)
        self.on_press_animation()
        thread_to_login = threading.Thread(target=self.login_edukacja_cl, args=())
        thread_to_login.start()


    pass
