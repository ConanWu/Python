#!usr/bin/python3
# -*- coding:utf-8 -*-

import unittest
from Test_Framework.test.case.test_baidu import TestBaidu

if __name__ == '__main__':
    suite = unittest.TestSuite()
    #tests = [TestBaidu('test_search_excel'), TestBaidu("test_add")]
    #suite.addTest(TestBaidu('test_search_excel'))
    #suite.addTests(tests)

    # execute all the test cases under the class
    cases = unittest.TestLoader().loadTestsFromTestCase(TestBaidu)
    suite = unittest.TestSuite([cases])
    #cases2=unittest.TestLoader().loadTestsFromTestCase(TestBaidu2)
    #suite=unittest.TestSuite([cases, cases2])

    suite.addTest(TestBaidu('execute_add'))
    # verbosity=2代表打印的日志级别
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


