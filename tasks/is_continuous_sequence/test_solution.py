import unittest
from solution import is_continuous_sequence

class TestIsContinuousSequence(unittest.TestCase):

    def test_valid_continuous_sequence(self):
        self.assertTrue(is_continuous_sequence([4, 5, 6, 7]))

    def test_valid_continuous_sequence_with_negatives(self):
        self.assertTrue(is_continuous_sequence([-3, -2, -1, 0]))

    def test_non_continuous_sequence(self):
        self.assertFalse(is_continuous_sequence([1, 3]))

    def test_single_element_sequence(self):
        self.assertFalse(is_continuous_sequence([10]))

    def test_empty_sequence(self):
        self.assertFalse(is_continuous_sequence([]))

    def test_sequence_with_non_integer(self):
        self.assertFalse(is_continuous_sequence([1, 2, '3']))

    def test_sequence_with_mixed_types(self):
        self.assertFalse(is_continuous_sequence([1, 2, None]))

    def test_sequence_with_floats(self):
        self.assertFalse(is_continuous_sequence([1.0, 2.0, 3.0]))

    def test_boolean_values(self):
        self.assertFalse(is_continuous_sequence([True, 2, 3]))
        self.assertFalse(is_continuous_sequence([False, 1, 2]))

if __name__ == '__main__':
    unittest.main()
