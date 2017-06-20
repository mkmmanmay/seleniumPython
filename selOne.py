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
driver.get("http://www.google.co.in")

print(driver.title)
search = driver.find_element_by_id("lst-ib")
search.send_keys("Inception movie")
search.send_keys(Keys.ENTER)
time.sleep(3)
#  http://selenium-python.readthedocs.io/getting-started.html
try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'res')))
    # (( )) is given because we are passing tuple of arguments
except Exception as e:
    print("Possible locator issue.")
finally:
    driver.quit()
