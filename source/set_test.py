#!python

from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set([1])
        assert test_set.size == 1

    def test_add(self):
        pass

    def test_remove(self):
        pass

    def test_contains(self):
        pass

    def test_union(self):
        pass

    def test_intersection(self):
        pass

    def test_difference(self):
        pass

    def test_subset(self):
        pass


if __name__ == '__main__':
    unittest.main()
