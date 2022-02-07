import booking.constant as const
import os
from selenium import webdriver

from booking.booking_filteration import BookingFiltration
from booking.booking_report import BookingReport

from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self , driver_path=r"C:\Users\india\Desktop\ChromeDriver" , teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        # ignoring or removing unwanted message during running selenium
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches' , ['enable-logging'])
        # since,its child class it need to instantiate parent class else error will occur.
        super(Booking , self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()
    
    def __exit__(self, *args) :
        if self.teardown :
            self.quit()
            print('Exiting ...')
    
    # DEAL SEARCHING
    
    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def change_currency(self,currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        
        """
        INR = India Rupees,
        USD = USA Dollar,
        CNY = Chinese Yuan,
        JPY = Japanese Yen , ...etc
        """

        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()
        
        
    def select_place_to_go(self , place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()# cleaning the text in field
        search_field.send_keys(place_to_go)
        
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()
        
    def select_dates(self , check_in_date,check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()
        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()
    
    def select_adults(self , count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()
        while True :
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()
            # if value of adults reaches 1 then we should
            #  get out of the while loop.
            adults_value_element = self.find_element_by_id('group_adults')
            # get_attribute() : 
            # get_attribute is basically a method that receives a key name
            # and then it tries to give you back the value of 
            # whatever attribute it is.
            adults_value = adults_value_element.get_attribute(
                'value'
            ) # should give back adults count
            if int(adults_value) == 1 :
                break
        
        increase_button_element= self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        
        # if you don't need to use variable in for loop then, just use '_' instead.
        for _ in range(count-1):
            increase_button_element.click()
    
    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()
        
        
    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(3)
        filtration.sort_price_lowest_first()
        
    def report_results(self):
        # hotel_boxes = self.find_element_by_id(
        #     'hotellist_inner'
        # )
        hotel_boxes = self.find_element_by_class_name('_fe1927d9e')

        report = BookingReport(hotel_boxes)
        # report.pull_titles()
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)
            
            
        
    




