from calculator import Count
import testfixture
import unittest

class TestIsPrime(testfixture.TestFixture):
    def test_prime1(self):
        j = Count(7, 9)
        self.assertTrue(j.is_prime(), msg='test failed')

    # def test_prime2(self):
    #     self.assertTrue((is_prime(7)), msg='test failed')