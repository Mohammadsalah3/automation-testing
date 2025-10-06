from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path=r"D:\QC_seleuinm\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://chatgpt.com/")

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "placeholder")))
search_box.send_keys("tell me about selenium" + Keys.ENTER)


"""
driver.get("https://www.google.co.uk/")


search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

search_box.send_keys("mo salah" + Keys.ENTER)

#search_box.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)
"""
"""
driver.get("https://application.bau.edu.jo/reg_new/index.jsp")

username_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username")) )
username_box.clear()
username_box.send_keys("user_name")
time.sleep(3)
password_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password")) )
password_box.clear()
password_box.send_keys("pass" + Keys.ENTER)
"""
time.sleep(20)
driver.quit()


