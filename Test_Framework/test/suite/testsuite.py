#!usr/bin/python3
# -*- coding:utf-8 -*-

import unittest
from Test_Framework.test.case.test_baidu import TestBaidu
from Test_Framework.utils.config import REPORT_PATH
from Test_Framework.utils.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':

    suite = unittest.TestSuite()
    # tests = [TestBaidu('test_search_0'), TestBaidu("test_search_1")]
    # suite.addTest(TestBaidu('test_search_0'))
    # suite.addTest(TestBaidu('test_search_1'))
    # suite.addTests(tests)

    # execute all the test cases under the class
    cases = unittest.TestLoader().loadTestsFromTestCase(TestBaidu)
    suite = unittest.TestSuite([cases])
    #cases2=unittest.TestLoader().loadTestsFromTestCase(TestBaidu2)
    #suite=unittest.TestSuite([cases, cases2])

    suite.addTest(TestBaidu('execute_add'))
    reportFile = (REPORT_PATH + '\\report1.html')
    with open(reportFile, 'wb') as r:
        # runner = unittest.TextTestRunner(verbosity=2)
        runner = HTMLTestRunner(r, verbosity=2, title='测试百度搜索1', description='修改报告1')
        runner.run(suite)

    #
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)



