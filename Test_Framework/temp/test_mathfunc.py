# -*- coding: utf-8 -*-

import unittest
from Test_Framework.temp.mathfunc import Mathfunc


class TestMathFunc(unittest.TestCase):

    def test_add(self):
        # x = Mathfunc()
        # self.assertEqual(3, x.add(1, 2))
        # self.assertNotEqual(3, x.add(2, 2))
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    def test_minus(self):
        x = Mathfunc()
        self.assertEqual(1, x.minus(3, 2))

    def test_multi(self):
        x = Mathfunc()
        self.assertEqual(6, x.multi(2, 3))

    def test_divide(self):
        x = Mathfunc()
        self.assertEqual(2, x.divide(6, 3))
        self.assertEqual(2.5, x.divide(5, 2))


if __name__ == '__main__':
    unittest.main()
