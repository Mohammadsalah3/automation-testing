from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="D:\QC_seleuinm\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(20)


WebDriverWait(driver, 160).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located((By.ID, "cookieAnchor"))
)

while True:
    cookie = driver.find_element(By.ID, "cookieAnchor")
    cookie.click()

time.sleep(10)
driver.quit()
    