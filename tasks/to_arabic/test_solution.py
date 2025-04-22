import unittest # Import the unittest module
from solution import to_arabic # Import the function from solution.py

class TestToArabicFunction(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    
    def test_valid_numerals(self): # Test case for valid Roman numerals
        self.assertEqual(to_arabic('I'), 1)         
        self.assertEqual(to_arabic('IV'), 4)        
        self.assertEqual(to_arabic('IX'), 9)        
        self.assertEqual(to_arabic('X'), 10)        
        self.assertEqual(to_arabic('XL'), 40)       
        self.assertEqual(to_arabic('XC'), 90)       
        self.assertEqual(to_arabic('C'), 100)       
        self.assertEqual(to_arabic('CD'), 400)      
        self.assertEqual(to_arabic('CM'), 900)      
        self.assertEqual(to_arabic('M'), 1000)      
        self.assertEqual(to_arabic('MMMCMXCIV'), 3994)  

    def test_invalid_numerals(self): # Test case for invalid Roman numerals
        self.assertEqual(to_arabic('IIII'), False)  
        self.assertEqual(to_arabic('VV'), False)    
        self.assertEqual(to_arabic('XXXX'), False)  
        self.assertEqual(to_arabic('LL'), False)   
        self.assertEqual(to_arabic('CCCC'), False)  
        self.assertEqual(to_arabic('DD'), False)    
        self.assertEqual(to_arabic('MMMM'), False)  
        self.assertEqual(to_arabic('XM'), False)    

    def test_empty_string(self): # Test case for empty string
        self.assertEqual(to_arabic(''), False)      

    def test_non_roman_characters(self): # Test case for non-Roman characters
        self.assertEqual(to_arabic('A'), False)     
        self.assertEqual(to_arabic('123'), False)   

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
