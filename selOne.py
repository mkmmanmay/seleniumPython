import os

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = "C:/browserdrivers/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get("http://qa.guru.com/login.aspx")
print(driver.title)
username = driver.find_element_by_xpath("//input[contains(@id, 'Login_txtUserName')]")
username.send_keys("gurufree001@gmail.com")
password = driver.find_element_by_xpath("//input[contains(@id, 'Login_txtPassword')]")
password.send_keys("12345678")
password.send_keys(Keys.ENTER)
#  http://selenium-python.readthedocs.io/getting-started.html
try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//label[contains(@id, 'ContentPlaceHolder')]")))
    # (( )) is given because we are passing tuple of arguments
except Exception as e:
    print("Possible locator issue.")

question = driver.find_element_by_xpath("//label[contains(@id, 'ContentPlaceHolder')]").text
answerBox = driver.find_element_by_xpath("//input[contains(@id, 'TextBox')]")
answerBox.send_keys(question)
answerBox.send_keys(Keys.ENTER)

try:
    section = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//section[@class='module_box dashboardSection top']")))
except Exception as e:
    print("Error is: ", e)
    print("Dashboard didn't load in time.")
finally:
    driver.quit()
