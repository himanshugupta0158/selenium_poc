"""
This file will include a class with instance methods.
that will be responsible to interact with our website
After , we have some results, to apply filterations.
"""

from lib2to3.pgen2 import driver
from selenium import webdriver
# this typing library is used for defining specific variable types .
from typing import List
# we can import driver's type using below selenium library
from selenium.webdriver.remote.webdriver import WebDriver 
#basically ,we are defining type webdriver of selenium



class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    # Need to improve below method 
    def apply_star_rating(self, *star_values):
        # star_filtration_box = self.driver.find_elements_by_class_name('')
        # star_child_elements = self.driver.find_elements_by_css_selector('div[class="_29c344764"]')
        star1 = self.driver.find_element_by_css_selector(
            'input[name="class=1"]'
        )
        star2 = self.driver.find_element_by_css_selector(
            'input[name="class=2"]'
        )
        star3 = self.driver.find_element_by_css_selector(
            'input[name="class=3"]'
        )
        star4 = self.driver.find_element_by_css_selector(
            'input[name="class=4"]'
        )
        star5 = self.driver.find_element_by_css_selector(
            'input[name="class=5"]'
        )
        
        
        
        # print(len(star_child_elements))
        
        for value in star_values : 
            if int(value) == 1:
                star1.click()
            elif int(value) == 2:
                star2.click()
            elif int(value) == 3:
                star3.click()
            elif int(value) == 4:
                star4.click()
            elif int(value) == 5:
                star5.click()
            
                

    def sort_price_lowest_first(self):
        element = self.driver.find_element_by_css_selector(
            'li[data-id="price"]',
            # 'a[class="a5b679fa41 "]',
        )
        element.click()   
        



