import unittest
from HTMLTestRunner import HTMLTestRunner
from test_case import test_baidu
from test_case import test_youdao

import time

# test_dir = './test_case'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
suite = unittest.TestSuite()

suite.addTest(test_baidu.MyTest("test_baidu"))
suite.addTest(test_baidu.MyTest("test_baidu2"))
suite.addTest(test_youdao.MyTestYoudao("test_baidu3"))
now = time.strftime("%Y_%m_%d %H_%M_%S")

if __name__ == '__main__':
    #runner = unittest.TextTestRunner()
    fp = open('report/' + now + 'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Test Baidu Search',
                            description='Baidu Test Result: ')
    runner.run(suite)
    fp.close()