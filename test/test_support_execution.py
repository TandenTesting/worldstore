#!/usr/bin/python

import unittest
from support import execution as execution

class test_execution_module(unittest.TestCase):

    def test_thinktime_noparam(self):
        print ('test_thinktime_noparam')
        pass

    def test_thinktime_underrange(self):
        print('test_thinktime_underrange')
        pass

    def test_thinktime_overrange(self):
        print('test_thinktime_overrange')
        pass

    def test_thinktime_inrange(self):
        print('test_thinktime_inrange')
        pass
        
    def test_thinktime_explict_none(self):
        print ('test_thinktime_noparam')
        pass
        
if __name__ == '__main__':
    unittest.main()