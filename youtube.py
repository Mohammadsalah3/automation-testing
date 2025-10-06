from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path=r"D:\QC_seleuinm\chromedriver.exe") 
driver = webdriver.Chrome(service=service)


driver.get("https://www.google.co.uk/")

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

search_box.send_keys("YouTube" + Keys.ENTER)
time.sleep(15)

first_result = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//div[@class='MjjYud']//a)[1]"))
)
first_result.click()
# pom version of this code :

class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")
        self.first_result = (By.XPATH, "(//div[@class='MjjYud']//a)[1]")

    def search(self, keyword):
        self.driver.find_element(*self.search_box).send_keys(keyword + "\n")

    def click_first_result(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_result)
        ).click()


time.sleep(10)
driver.quit()
