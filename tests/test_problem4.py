from unittest import TestCase

from problem4 import largest_palindrome_num


class Test(TestCase):
    def test_largest_palindrome_num_example(self):
        self.assertEqual(9009, largest_palindrome_num(2))
