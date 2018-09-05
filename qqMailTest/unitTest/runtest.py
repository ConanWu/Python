import unittest
import testadd
import testisprime
from HTMLTestRunner import HTMLTestRunner

#构造测试集
suite = unittest.TestSuite()

suite.addTest(testadd.TestAdd("test_add1"))
suite.addTest(testadd.TestAdd("test_add2"))
suite.addTest(testisprime.TestIsPrime("test_prime1"))


if __name__ == '__main__':
    # runner = unittest.TextTestRunner()

    #定义报告存放路径
    fp = open('./result.html', 'wb')

    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='Baidu Testing',
                            description='Testing Result: ')
    runner.run(suite)
    fp.close()