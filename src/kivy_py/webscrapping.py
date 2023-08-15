from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_usos():
    login_url = "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex&locale=pl"

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # headless - web browser without graphic interface
    driver = webdriver.Firefox(options=options)

    try:
        # Get site after login
        print("LOGGING IN")
        driver.get("https://web.usos.pwr.edu.pl/kontroler.php?_action=katalog2/przedmioty/wybierzGrupePrzedmiotow&jed_org_kod=W12N&callback=g_5e872193&tab_offset=30&tab_limit=30&tab_order=2a1a")
        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "PO-W12-AIR---ST-Ii-WRO"))
    )
        element.find_element(By.PARTIAL_LINK_TEXT, "Lista przedmiotów").click()

        with open("output.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

    finally:
        driver.quit()

login_usos()
