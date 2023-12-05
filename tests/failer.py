import unittest

class Fail(unittest.TestCase):
    
    def test_fail(self):
        self.assertEqual(True, False, "The purpose of this test is to fail.")