from calculator import Count

import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        print('Test case Start')

    def tearDown(self):
        print('Test case end')

#test add function
class TestCount(MyTest):

    def test_str(self):
        a = "Hello"
        b = "Hello World"
        self.assertIn(a, b, msg='b not include a')

#excute test class
# mytest = TestCount()
# mytest.test_add()

# if __name__ == '__main__':
#     unittest.main()
# collect test suite
suite = unittest.TestSuite()
suite.addTest(TestCount("test_prime"))
suite.addTest(TestCount("test_str"))

# run test suite
runner = unittest.TextTestRunner()
runner.run(suite)
