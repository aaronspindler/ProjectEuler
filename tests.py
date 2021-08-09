from unittest import TestCase

from problem1 import sum_multi_3_and_5
from problem2 import fib_sum_even
from problem3 import largest_prime_factor
from problem4 import largest_palindrome_num
from problem5 import smallest_divisable_by_range
from problem6 import sum_square_difference
from problem7 import n_prime
from problem8 import largest_product


class Test(TestCase):
    def test_sum_multi_3_and_5_example(self):
        self.assertEqual(23, sum_multi_3_and_5(10))

    def test_fib_sum_even_example(self):
        self.assertEqual(44, fib_sum_even(89))

    def test_largest_prime_factor_example(self):
        self.assertEqual(29, largest_prime_factor(13195))

    def test_largest_palindrome_num_example(self):
        self.assertEqual(9009, largest_palindrome_num(2))

    def test_smallest_divisable_by_range_example(self):
        self.assertEqual(2520, smallest_divisable_by_range(10))

    def test_sum_square_difference_example(self):
        self.assertEqual(2640, sum_square_difference(10))

    def test_n_prime_example(self):
        self.assertEqual(13, n_prime(6))

    def test_largest_product_example(self):
        self.assertEqual(5832, largest_product(4))
