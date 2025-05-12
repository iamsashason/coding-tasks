Implement and export the ip2int and int2ip functions, which convert the dotted-decimal representation of an IP address to a 32-bit dotted-decimal number and back. The ip2int function takes an input signal and must return a number. The int2ip function is the opposite: it takes an input number and returns the result.
Examples:
ip2int('128.32.10.1') # 2149583361
ip2int('255.255.255.255') # 4294967295
int2ip(2149583361) # '128.32.10.1'
int2ip(4294967295) # '255.255.255.255'