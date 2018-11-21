#!usr/bin/python3
# -*- coding:utf-8 -*-

import unittest


class Assertion(unittest.TestCase):

    @staticmethod
    def assert_compare(expert_result, actual_result):
        if expert_result == actual_result:
            Assertion.assertEqual(expert_result, actual_result)
            print('assertion by Lin')
        else:
            raise AssertionError('compare failed, expert_result is :' + str(expert_result) + 'actual_result is : ' + str(actual_result))

    @staticmethod
    def assert_http_response(response, code_list=None):
        res_code = response.status_code
        if not code_list:
            code_list = [200]
        if res_code not in code_list:
            raise AssertionError('response code not in list')