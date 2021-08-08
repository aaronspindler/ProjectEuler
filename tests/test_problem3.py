from unittest import TestCase

from problem3 import largest_prime_factor


class Test(TestCase):
    def test_largest_prime_factor_example(self):
        self.assertEqual(29, largest_prime_factor(13195))
