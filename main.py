import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"D:/chromedriver-win64"
driver = webdriver.Chrome()

driver.get("https://roots.smashy.space/")
my_element = driver.find_element(By.CSS_SELECTOR,".pre-footer .button-wrapper a")
# print(my_element)

size = my_element.size
w, h = size['width'], size['height']

print('width',w)
print('height',h)
