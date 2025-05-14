Implement the predicate function is_valid_ipv6, which checks IPv6 (Internet Protocol version 6) addresses for validity. The function takes a string with an IPv address as input and returns True if the address is valid and False otherwise.
Additional conditions:
• The function is case-insensitive.
• Leading zeros in groups of digits are optional.
• The longest sequence of groups of zeros, for example, :0:0:0: can be replaced by two colons : :.
Such a replacement can be made only once.
• One group of zeros : 0: cannot be replaced by ::.
Examples:
is_valid_ipv6('10:d3:2d06:24:400c:5ee0:be: 3d*) # True
is_valid_ipv6('::1') # True
is_valid_ipv6('2607:G8B0:4010:801: :1004') # False
is_valid_ipv6('2.001::') # False