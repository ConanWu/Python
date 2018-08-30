from calculator import Count
import testfixture
import unittest

class TestAdd(testfixture.TestFixture):

    def test_add1(self):
        try:
            j = Count(2, 3)         # initial class Count
            add = j.add()           # call add function
            assert(add == 5), 'Integer addition result error!'
        except AssertionError as msg:
            print(msg)
        else:
            print('test pass!')

    def test_add2(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5, msg='test failed')

if __name__ == '__main__':
    unittest.main()
