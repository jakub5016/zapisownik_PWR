from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def login_edukacja_cl(username, password):
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

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        driver.implicitly_wait(10)
        print("LOGIN COMPLETE")
        # Go to zapisy
        print("GOING TO \"ZAPISY\"")
        driver.find_element(By.XPATH, "//*[contains(text(), 'Zapisy')]").click()

        driver.implicitly_wait(10)

        with open("output.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

        print("Zawartość strony została zapisana do pliku 'output.html'.")

    finally:
        driver.quit()
