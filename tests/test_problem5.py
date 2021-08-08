from unittest import TestCase

from problem5 import smallest_divisable_by_range


class Test(TestCase):
    def test_smallest_divisable_by_range_example(self):
        self.assertEqual(2520, smallest_divisable_by_range(10))
