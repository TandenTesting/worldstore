#!/usr/bin/python

import unittest
import logging
import json

from support import execution
from support import config
from support.generate import  id_generator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Test_Newsletter_Negative_Validation(unittest.TestCase):
    """ %%Test ID%% WS-01-001-N
        %%Test Suite%% Email Validation
        %%Test Name%% Test Newsletter Negative Validation
        To verify that entering an invalid email address into the email signup field and trying to 
        submit this email address will result in an error message.
        Note: Not included but should also check that this email is not registered at the server
    """
    def setUp(self):
        """ %%Precondition%% Determine the correct url to be tested, determine from given SUT
        """
        with open("_config/site.json") as json_file:
            test_conf = json.load(json_file)
        self.driver = webdriver.Firefox()
        self.env=execution.environment('_config/execution.json').get_testenv()
        self.site = test_conf[self.env]['URL']
        logging.info('Testing against {} base url {}'.format(self.env, self.site))

    def tearDown(self):
        self.driver.close()

    def test_email_bad(self):
        """ %%#1 Action%% Navigate to site
            %%#1 Expected%% Site is displayed in browser
        """
        self.driver.get(self.site)
        logging.info('Testing Page title {}'.format(self.driver.title))
        assert "Modern - Modern.co.uk" in self.driver.title
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-01-001-N-001.png'))
        self.driver.save_screenshot('_evidence/WS-01-001-N-001.png')
        """ %%#2 Action%% Locate newsletter entry & fill in bad email
            %%#2 Expected%% Entery textbox can be found on the page and email address can be entered
        """
        self.elem = self.driver.find_element_by_id('newsletter-email') 
        self.elem.send_keys('user@127.0.0.1')
        """ %%#3 Action%% Submit email address for page level validiation
            %%#3 Expected%% Submit action causes page to update with status of check on email
        """
        self.elem.submit()
        logging.info('Testing Screenshot bad email found at {}'.format('_evidence/WS-01-001-N-002.png'))
        self.driver.save_screenshot('_evidence/WS-01-001-N-002.png')
        """ %%#4 Action%% Check message is displayed in html div 'newsletter-signup-errormsg' 
            %%#4 Expected%% Correct message is in fact found in the correct DOM location.
        """
        self.elem = self.driver.find_element_by_class_name('newsletter-signup-errormsg')
        logging.info('Testing Pagetext @newsletter-signup-errormsg =  {}'.format(self.elem.text))
        assert 'Invalid email address' in self.elem.text

class Test_Newsletter_Positive_Validation(unittest.TestCase):
    """ %%Test ID%% WS-01-002-P
        %%Test Suite%% Email Validation
        %%Test Name%% Test Newsletter Positive Validation
        To verify that entering a valid email address into the email signup field and trying to 
        submit this email address will result in a **TO_DO**.
        Note: Not included but should also check that this email is registered at the server, and 
              subsquent notifications are sent
    """
    def setUp(self):
        """ %%Precondition%% Determine the correct url to be tested, determine from given SUT
        """
        with open("_config/site.json") as json_file:
            test_conf = json.load(json_file)
        self.driver = webdriver.Firefox()
        self.env=execution.environment('_config/execution.json').get_testenv()
        self.site = test_conf[self.env]['URL']
        logging.info('Testing against {} base url {}'.format(self.env, self.site))

    def tearDown(self):
        self.driver.close()  
            
    def test_email_good(self):
        """ %%#1 Action%% Navigate to site
            %%#1 Expected%% Site is displayed in browser
        """
        self.driver.get(self.site)
        logging.info('Testing Page title {}'.format(self.driver.title))
        assert "Modern - Modern.co.uk" in self.driver.title
        logging.info('Testing Screenshot found at {}'.format('_evidence/WS-01-002-P-001.png'))
        self.driver.save_screenshot('_evidence/WS-01-002-P-001.png')
        """ %%#2 Action%% Locate newsletter entry & fill in bad email
            %%#2 Expected%% Entry textbox can be found on the page and email address can be entered
        """
        self.elem = self.driver.find_element_by_id('newsletter-email')
        emailname = id_generator()
        logging.info('Testing Data email used {}@gmail.com'.format(''.join (emailname)))
        self.elem.send_keys(emailname + '@gmail.com')

        """ %%#3 Action%% Submit email address for page level validiation
            %%#3 Expected%% Submit action causes page to update with status of check on email
        """
        self.elem.submit()
        # need this delay due to server round trip
        self.wait = WebDriverWait(self.driver, 10)
        self.elem = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'newsletter-signup-successmsg')))
        # Now element present take screen shot, and do check 
        logging.info('Testing Screenshot good email found at {}'.format('_evidence/WS-01-002-P-002.png'))
        self.driver.save_screenshot('_evidence/WS-01-002-P-002.png')

        """ %%#4 Action%% Check message is displayed in html div 'newsletter-signup-successmsg' 
            %%#4 Expected%% Correct message is in fact found in the correct DOM location.
        """
        logging.info('Testing Pagetext @newsletter-signup-successmsg =  {}'.format(self.elem.text))
        assert 'Email address subscribed' in self.elem.text

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s: %(levelname)s - %(message)s', 
                        filename='_evidence/' + config.logfile('_config/execution.json') + '.log',
                        level=logging.DEBUG ) 
    unittest.main()