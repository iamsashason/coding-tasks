import unittest # Import the unittest module
from solution import is_valid_ipv6 # Import the function from solution.py

class TestIsValidIPv6(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_valid_addresses(self): # Define a test method to check valid IPv6 addresses
        self.assertTrue(is_valid_ipv6('10:d3:2d06:24:400c:5ee0:be:3d'))
        self.assertTrue(is_valid_ipv6('::1'))  # loopback
        self.assertTrue(is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))
        self.assertTrue(is_valid_ipv6('2001:db8:85a3::8a2e:370:7334'))
        self.assertTrue(is_valid_ipv6('0:0:0:0:0:0:0:1'))
        self.assertTrue(is_valid_ipv6('::'))  # unspecified address
        self.assertTrue(is_valid_ipv6('fe80::1ff:fe23:4567:890a'))
        self.assertTrue(is_valid_ipv6('2001:db8::1:0:0:1'))

    def test_invalid_addresses(self): # Define a test method to check invalid IPv6 addresses
        self.assertFalse(is_valid_ipv6('2607:G8B0:4010:801::1004'))  # Invalid hex 'G'
        self.assertFalse(is_valid_ipv6('2.001::'))  # Contains IPv4-like section
        self.assertFalse(is_valid_ipv6('2001::25de::cade'))  # Double '::'
        self.assertFalse(is_valid_ipv6('2001:0db8:85a3:0:0:8A2E:0370:7334:1234'))  # Too many groups
        self.assertFalse(is_valid_ipv6('2001:db8:85a3'))  # Too few groups without ::
        self.assertFalse(is_valid_ipv6('2001:db8:::1'))  # Triple colon
        self.assertFalse(is_valid_ipv6('abcd:12345::'))  # Group too long
        self.assertFalse(is_valid_ipv6('abcd::g123'))  # Invalid character 'g'

    def test_case_insensitivity(self): # Define a test method to check case insensitivity
        self.assertTrue(is_valid_ipv6('ABCD:ef01:2345:6789:ABCD:EF01:2345:6789'))

    def test_only_zeros(self): # Define a test method to check addresses with only zeros
        self.assertTrue(is_valid_ipv6('0:0:0:0:0:0:0:0'))
        self.assertTrue(is_valid_ipv6('::'))

    def test_one_group_zero_not_compressed(self): # Define a test method to check addresses with one group of zeros not compressed
        self.assertTrue(is_valid_ipv6('1:2:3:4:5:6:0:8'))

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
