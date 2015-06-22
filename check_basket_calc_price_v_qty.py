#!/usr/bin/python

import unittest
import logging
import json
import time

from support import execution
from support.generate import  id_generator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Test_Basket_Price_and_Qty(unittest.TestCase):
    """ %%Test ID%% WS-02-001-P
        %%Test Suite%% Basket Validation
        %%Test Name%% Test_Basket_Price_and_Qty
        To verify that the operation of the basket Price versus Quantity calculation is working
    """
    def setUp(self):
        """ %%Precondition%% Determine the correct url to be tested, determine from given SUT,
        """
        with open("_config/site.json") as json_file:
            test_conf = json.load(json_file)
        self.driver = webdriver.Firefox()
        self.env=execution.environment('_config/execution.json').get_testenv()
        self.site = test_conf[self.env]['URL']
        logging.info('Testing against {} base url {}'.format(self.env, self.site))

    def tearDown(self):
        self.driver.close()

    def test_price_vs_qty(self):
        """ %%#1 Action%% Navigate to site
            %%#1 Expected%% Site is displayed in browser
        """
        self.driver.get(self.site)
        logging.info('Testing Page title {}'.format(self.driver.title))
        assert "Modern - Modern.co.uk" in self.driver.title
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-02-001-P-001.png'))
        self.driver.save_screenshot('_evidence/WS-02-001-P-001.png')
        
        """ %%#2 Action%% navigate to Prodduct page
            %%#2 Expected%% Product must be available
        """
        self.driver.get(self.site+'/p/Bravura_Taupe_Rug.htm')
        assert "Bravura Taupe Rug" in self.driver.title
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-02-001-P-002.png'))
        self.driver.save_screenshot('_evidence/WS-02-001-P-002.png')
        
        """ %%#3 Action%% Click the "add to the basket" link
            %%#3 Expected%% Item should be added to the basket
        """
        self.elem = self.driver.find_element_by_id('ws-btnaddcart') 
        self.elem.click()
        time.sleep(1) # time for cart to register (only to get screen shot)
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-02-001-P-003.png'))
        self.driver.save_screenshot('_evidence/WS-02-001-P-003.png')
        
        """ %%#4 Action%% navigate to the basket 
            %%#4 Expected%% Basket page is loaded with only one item in
        """
        self.driver.find_element_by_partial_link_text('Basket').click()
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-02-001-P-004.png'))
        self.driver.save_screenshot('_evidence/WS-02-001-P-004.png')
        assert "Shopping Cart" in self.driver.title
        items = self.driver.find_elements_by_class_name('order_products')
        self.assertEqual(1,len(items))

        """ %%#5 Action%% Confirm item total is the same as line total
            %%#5 Expected%% line and item total are the same
        """
        # the following is really messy, It could be done a lot better by giving the inventory lines a class
        self.basket = self.driver.find_element_by_name("basket")
        self.rows = self.basket.find_elements(By.TAG_NAME, "tr")
        self.itemcost = self.rows[1].find_elements(By.TAG_NAME, "td")
        self.assertEqual(float(self.itemcost[1].text.strip()[1:]), float(self.itemcost[3].text.strip()[1:]))

        """ %%#6 Action%% increase product count to 2 
            %%#6 Expected%% line total is not twice single item total
        """
        self.select = Select(self.itemcost[2].find_element_by_name('quantity'))
        self.select.select_by_visible_text('2')
        self.driver.switch_to_alert().accept()
        self.basket = self.driver.find_element_by_name("basket")
        self.rows = self.basket.find_elements(By.TAG_NAME, "tr")
        self.itemcost = self.rows[1].find_elements(By.TAG_NAME, "td")
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-02-001-P-005.png'))
        self.driver.save_screenshot('_evidence/WS-02-001-P-005.png')
        self.assertEqual(float(self.itemcost[1].text.strip()[1:])*2.0, float(self.itemcost[3].text.strip()[1:]))

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s: %(levelname)s - %(message)s', 
                        filename='_evidence/' + lconfig.logfile('_config/execution.json') + '.log',
                        level=logging.DEBUG ) 
    unittest.main()