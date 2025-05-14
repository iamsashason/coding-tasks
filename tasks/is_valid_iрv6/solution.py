#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.
import re

def is_valid_ipv6(address):
    if not address or address.count('::') > 1:
        return False

    if '::' in address:
        head, _, tail = address.partition('::')
        head_groups = head.split(':') if head else []
        tail_groups = tail.split(':') if tail else []
        num_insert = 8 - (len(head_groups) + len(tail_groups))
        if num_insert < 1:
            return False  
        groups = head_groups + (['0'] * num_insert) + tail_groups
    else:
        groups = address.split(':')
        if len(groups) != 8:
            return False

    for group in groups:
        if not (1 <= len(group) <= 4):
            return False
        if not re.fullmatch(r'[0-9a-fA-F]+', group):
            return False

    return True

def main(): # Main function to execute the program.
    print(is_valid_ipv6('10:d3:2d06:24:400c:5ee0:be:3d'))      # True
    print(is_valid_ipv6('::1'))                                # True
    print(is_valid_ipv6('2607:G8B0:4010:801::1004'))           # False 
    print(is_valid_ipv6('2.001::'))                            # False 
    print(is_valid_ipv6('2001:db8::1:0:0:1'))                  # True
    print(is_valid_ipv6('2001:db8:0:0:0:0:2:1'))               # True
    print(is_valid_ipv6('2001:db8::2:1'))                      # True

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.