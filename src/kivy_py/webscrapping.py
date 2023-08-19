from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_usos():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # headless - web browser without graphic interface
    driver = webdriver.Firefox(options=options)

    try:
        code = "5I-AIR-000"
        web_addres = "https://web.usos.pwr.edu.pl/kontroler.php?_action=katalog2%2Fprzedmioty%2FpokazPlanGrupyPrzedmiotow&grupa_kod=" + code + "&cdyd_kod=2023%2F24-Z&fbclid=IwAR1Aviwa3sgYY5RtHBmpLHnMuQoycWX438JvQ8Zw-2cbrhzNrRUPSi_MAvk"
        driver.get(web_addres)

        courses_list = driver.find_element(By.XPATH, "/html/body/usos-layout/div[2]/main-panel/main/div/div/div[5]/div/div[2]/map")

        links_full = courses_list.find_elements(By.TAG_NAME, "area")

        links =[]

        for link in links_full:
            href = link.get_attribute("href")
            links.append(href)

        for link in links:
            driver.get(link)
            # print(link)
            print(driver.find_element(By.XPATH, "/html/body/usos-layout/div[2]/main-panel/main/div/div/table/tbody/tr[1]/td[2]/a").get_attribute("text"))
            print(driver.find_element(By.XPATH, "/html/body/usos-layout/div[2]/main-panel/main/div/div/table/tbody/tr[8]/td[2]/a").get_attribute("text"))
            print(driver.find_element(By.XPATH, "/html/body/usos-layout/div[2]/main-panel/main/div/div/h1/span[3]").text)
            print(driver.find_element(By.XPATH, "/html/body/usos-layout/div[2]/main-panel/main/div/div/table/tbody/tr[3]/td[2]/div").text)
            
            print("\n")
        with open("output.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

    finally:
        driver.quit()

login_usos()
