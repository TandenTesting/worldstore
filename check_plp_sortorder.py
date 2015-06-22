#!/usr/bin/python

import unittest
import logging
import json
import time

from support import config
from support import execution
from support.generate import  id_generator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Test_PLP_SortOrder(unittest.TestCase):
    """ %%Test ID%% WS-03-001-P
        %%Test Suite%% Product Listing Page
        %%Test Name%% Test_PLP_sortorder
        To verify that the operation of the Product Listing Page (plp) sort order is working
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

    def test_plp_order_by_price(self):
        """ %%#1 Action%% Navigate to site
            %%#1 Expected%% Site is displayed in browser
        """
        self.driver.get(self.site)
        logging.info('Testing Page title {}'.format(self.driver.title))
        assert "Modern - Modern.co.uk" in self.driver.title
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-04-001-P-001.png'))
        self.driver.save_screenshot('_evidence/WS-04-001-P-001.png')

        """ %%#2 Action%% navigate to Product Listing Page
            %%#2 Expected%% Product category must have more than 2 items with different stock price
        """
        self.driver.get(self.site+'/c/Modern_Plain_Rugs.htm')
        assert "Modern Plain Rugs" in self.driver.title
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-04-001-P-002.png'))
        self.driver.save_screenshot('_evidence/WS-04-001-P-002.png')

        """ %%#3 Action%% Sort PLP Low to High
            %%#3 Expected%% items are in ascending order
        """
        self.select = Select(self.driver.find_element_by_class_name('sorts')) # form has the same name as select box 
        self.select.select_by_visible_text('Price: Low to High')
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-04-001-P-003.png'))
        self.driver.save_screenshot('_evidence/WS-04-001-P-003.png')
        self.items_on_page = self.driver.find_elements(By.CLASS_NAME, 'products-list-item-container')
        item_prices = []
        for idx in self.items_on_page:
            price=float(idx.find_element_by_class_name('item-price').text.strip()[1:])
            item_prices.append(price)
        logging.info('Testing PLP ascending order. Prices = {}'.format(item_prices))
        self.assertEqual(item_prices, sorted(item_prices))

        """ %%#4 Action%% Sort PLP High to Low
            %%#4 Expected%% items are in descending order
        """
        self.select = Select(self.driver.find_element_by_class_name('sorts')) # form has the same name as select box 
        self.select.select_by_visible_text('Price: High to Low')
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-04-001-P-004.png'))
        self.driver.save_screenshot('_evidence/WS-04-001-P-004.png')
        self.items_on_page = self.driver.find_elements(By.CLASS_NAME, 'products-list-item-container')
        item_prices = []
        for idx in self.items_on_page:
            price=float(idx.find_element_by_class_name('item-price').text.strip()[1:])
            item_prices.append(price)
        logging.info('Testing PLP descending order. Prices = {}'.format(item_prices))
        self.assertEqual(item_prices, sorted(item_prices, reverse=True))

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s: %(levelname)s - %(message)s', 
                        filename='_evidence/' + config.logfile('_config/execution.json') + '.log',
                        level=logging.DEBUG ) 
    unittest.main()