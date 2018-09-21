import collections
import os
import unittest

import main

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.logAnalyzer = main.LogAnalyzer(
            os.path.join(os.path.dirname(__file__), 'sample.log'))
        self.userDaily = collections.OrderedDict([('01-01-2018', 2), ('01-02-2018', 0), 
                                      ('01-03-2018', 1), ('01-04-2018', 0), 
                                      ('01-05-2018', 1)])
        
    def test_requests(self):
        self.assertEqual(4, self.logAnalyzer.requests())
    
    def test_errors(self):
        self.assertEqual(1, self.logAnalyzer.errors())
    
    def test_users(self):
        self.assertEqual(2, self.logAnalyzer.users())
    
    def test_days(self):
        self.assertEqual(5, self.logAnalyzer.days())

    def test_users_daily(self):
        self.assertEqual(self.userDaily, self.logAnalyzer.users_daily())
    

if __name__ == '__main__':
    unittest.main()