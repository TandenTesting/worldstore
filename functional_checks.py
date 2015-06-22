#!/usr/bin/python

import unittest
import logging
from support.generate import get_uuid1

from check_newsletter_email_validation import *
from check_basket_calc_price_v_qty import *
from check_plp_sortorder import *

# List of in scope tests
run_these = [
                Test_Newsletter_Positive_Validation,
                Test_Newsletter_Negative_Validation,
                Test_Basket_Price_and_Qty,
                Test_PLP_SortOrder
            ]

if __name__ == '__main__':
    execution_id =get_uuid1()
    logfile = config.logfile('_config/execution.json')+'.log'
    logging.basicConfig(format='%(asctime)s: %(levelname)s - %(message)s', 
                        filename='_evidence/' + logfile,
                        level=logging.DEBUG )
    logging.info('Testing Start execution id {}'.format(execution_id))
    tests = unittest.TestSuite()
    for test in run_these:
        tests.addTest(unittest.makeSuite(test))
    unittest.TextTestRunner().run(tests)
    logging.info('Testing Finish execution id {}'.format(execution_id))
