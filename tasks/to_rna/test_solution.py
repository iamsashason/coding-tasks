import unittest # Import the unittest module
from solution import to_rna # Import the function from solution.py

class TestToRna(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_standard_sequence(self): # Test the standard DNA sequence
        self.assertEqual(to_rna("ACGTGGTCTTAA"), "UGCACCAGAAUU")

    def test_empty_string(self): # Test the empty string case
        self.assertEqual(to_rna(""), "")

    def test_single_nucleotides(self): # Test single nucleotide cases
        self.assertEqual(to_rna("A"), "U")
        self.assertEqual(to_rna("C"), "G")
        self.assertEqual(to_rna("G"), "C")
        self.assertEqual(to_rna("T"), "A")

    def test_repeated_nucleotides(self): # Test repeated nucleotides
        self.assertEqual(to_rna("AAAA"), "UUUU")
        self.assertEqual(to_rna("CCCC"), "GGGG")

    def test_invalid_nucleotide_raises_keyerror(self): # Test invalid nucleotide raises KeyError
        with self.assertRaises(KeyError):
            to_rna("ABCD")

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
