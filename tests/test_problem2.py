from unittest import TestCase

from problem2 import fib_sum_even


class Test(TestCase):
    def test_fib_sum_even_example(self):
        self.assertEqual(44, fib_sum_even(89))
