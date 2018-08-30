import unittest

class TestFixture(unittest.TestCase):
    def setUp(self):
        print('Test case Start')

    def tearDown(self):
        print('Test case end')