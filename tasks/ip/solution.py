#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def ip2int(ip):
    parts = ip.split('.')
    return sum(int(part) << (8 * (3 - i)) for i, part in enumerate(parts))

def int2ip(ip_int):
    return '.'.join(str((ip_int >> (8 * i)) & 0xFF) for i in reversed(range(4)))

def main(): # Main function to execute the program.
    print(ip2int('128.32.10.1'))      # 2149583361
    print(ip2int('0.0.0.0'))          # 0
    print(ip2int('255.255.255.255'))  # 4294967295
    print(int2ip(2149583361))         # '128.32.10.1'
    print(int2ip(0))                  # '0.0.0.0'
    print(int2ip(4294967295))         # '255.255.255.255'

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.