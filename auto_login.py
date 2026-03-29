from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

uname = driver.find_element(By.ID, "username")
pword = driver.find_element(By.ID, "password")

uname.send_keys("tomsmith")
pword.send_keys("SuperSecretPassword!")

btn = driver.find_element(By.CSS_SELECTOR, "button.radius")
btn.click()

time.sleep(3)

btn2 = driver.find_element(By.CSS_SELECTOR, "a.radius")
btn2.click()

time.sleep(2)

