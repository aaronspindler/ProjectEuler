from unittest import TestCase

from problem1 import sum_multi_3_and_5


class Test(TestCase):
    def test_sum_multi_3_and_5_example(self):
        self.assertEqual(23, sum_multi_3_and_5(10))
