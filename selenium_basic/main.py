import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specifying Chromedriver path
os.environ["PATH"] += r"C:\Users\india\Desktop\ChromeDriver"

driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/manual-testing")
#waiting for 30 sec since loading website may take time but will not wait if element is already there.
# it also set for all element in selenium
driver.implicitly_wait(30) 
# my_element = driver.find_element_by_class_name('dropdown-toggle')
my_element = driver.find_element_by_class_name('leaf')
my_element.click()

# Another/Alternate way to find element in web page with wait if element is not there.
WebDriverWait(driver , 30).until(
    EC.text_to_be_present_in_element(
        #Element Filteration
        (By.CLASS_NAME, 'dropdown-toggle'),
        #The expected text
        'Complete!'
    )
)










