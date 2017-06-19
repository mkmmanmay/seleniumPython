import os

from selenium import webdriver

chromedriver = "C:/browserdrivers/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.google.co.in")
driver.maximize_window()
print(driver.title)