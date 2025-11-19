import unittest

from main import min_of_three_vars


class MinOfThreeVarsTestCase(unittest.TestCase):

    def test_min_a(self):
        result = min_of_three_vars(1, 2, 3)
        self.assertEqual(result, 1)

    def test_min_b(self):
        result = min_of_three_vars(5, 2, 7)
        self.assertEqual(result, 2)

    def test_min_c(self):
        result = min_of_three_vars(10, 15, 8)
        self.assertEqual(result, 8)

