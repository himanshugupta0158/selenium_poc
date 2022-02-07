""" 
This file is going to include method that will parse the 
specific data that we need from each one of the deal boxes.
"""

from selenium.webdriver.remote.webelement import WebElement


# Need to change some id and class of the html tag to existing tags.
class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_class_name('_7192d3184')

    def pull_titles(self):
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element_by_css_selector(
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            print(hotel_name)

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element_by_css_selector(
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            
            hotel_price = deal_box.find_element_by_class_name(
                'bui-price-display__value'
            ).get_attribute('innerHTML').strip()
            
            hotel_score = deal_box.get_attribute(
                'data-score'
            ).strip()

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection          
