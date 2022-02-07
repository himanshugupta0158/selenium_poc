import os
import time
from selenium import webdriver

# sending or using keys like : ctrl , Alt , Shift ,etc.. using selenium
from selenium.webdriver.common.keys import Keys

# TOPIC : Sending keys and CSS selector
# below is path for django-admin
# http://127.0.0.1:8000/admin/login/?next=/admin/

os.environ["PATH"] += r"C:\Users\india\Desktop\ChromeDriver"
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

# wait for 5 seconds
driver.implicitly_wait(5)

# accessing username field
username = driver.find_element_by_id("id_username")
# accessing password field
password = driver.find_element_by_id("id_password")
# accessing login button using div's class name
login = driver.find_element_by_class_name("submit-row")

# sending username value to username field
username.send_keys("admin")
# sending password value to password field
password.send_keys("1234")

# Now , clicking login button to logining in using above value.
# login.click()

# Now trying to click Enter after filling password field
# password.send_keys("1234" , Keys.ENTER)
""" 
Using Keys method , we can access keys like :
ENTER , SHIFT , CONTROL , ALTER , TAB , NUMPAD0,1...9 , 
INSERT , etc...
"""
# its successful bro .... hahahaha .....

""" 
css_selector  : 
find element using css_selector, we can access specific html
element with same tag but using different css value or attribute.
"""
# trying to access login button using css_selector
btn = driver.find_element_by_css_selector('input[value="Log in"]')
btn.click()

# 5seconds of delay to logging out of django-admin.
time.sleep(5)

# Logging out of the django-admin after 5 seconds.
driver.get("http://127.0.0.1:8000/admin/")
logout = driver.find_element_by_css_selector('a[href="/admin/logout/"]')
logout.click()