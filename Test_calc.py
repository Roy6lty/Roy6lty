import unittest
import calc

class TestCal (unittest.TestCase):
    def test_add(self):
        result = Test_calc.add(10,5)
        self.assertEqual(result, 15)