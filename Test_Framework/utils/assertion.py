#!usr/bin/python3
# -*- coding:utf-8 -*-

import unittest

class Assertion(unittest.TestCase):

    def assert_compare(self, expert_result, actual_result):
        if expert_result == actual_result:
            self.assertEqual()
        else:
            raise AssertionError('failed')