import unittest # Import the unittest module
from solution import ip2int, int2ip # Import the function from solution.py

class TestIPConversion(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    
    def test_ip2int(self): # Test method to check the ip2int function
        self.assertEqual(ip2int('128.32.10.1'), 2149583361)
        self.assertEqual(ip2int('0.0.0.0'), 0)
        self.assertEqual(ip2int('255.255.255.255'), 4294967295)
        self.assertEqual(ip2int('192.168.1.1'), 3232235777)
        self.assertEqual(ip2int('8.8.8.8'), 134744072)
    
    def test_int2ip(self): # Test method to check the int2ip function
        self.assertEqual(int2ip(2149583361), '128.32.10.1')
        self.assertEqual(int2ip(0), '0.0.0.0')
        self.assertEqual(int2ip(4294967295), '255.255.255.255')
        self.assertEqual(int2ip(3232235777), '192.168.1.1')
        self.assertEqual(int2ip(134744072), '8.8.8.8')
    
    def test_ip2int_and_int2ip(self): # Test method to check the round-trip conversion
        ip_addresses = ['128.32.10.1', '0.0.0.0', '255.255.255.255', '192.168.1.1', '8.8.8.8']
        for ip in ip_addresses:
            self.assertEqual(ip, int2ip(ip2int(ip)))

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
