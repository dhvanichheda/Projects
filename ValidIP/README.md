Basic Python project to parse valid IP addresses from a file containing values per line

There are 2 types of IP addresses - 
1. IPv4
2. IPv6

Format of a valid IPv4 address - 0.0.0.0
Conditions for validity :
1. 4 integers separated by periods 
2. The integers should have values between 0 and 255


Format of a valid IPv6 address - x:x:x:x:x:x:x:x 
Conditions for validity :
1. 8 hex values (16 bits each) seperated by colon
2. x can range between 0000 to ffff. 
Edge cases for ipv6:
1. compressed - 2001:db8::1 (there cannot be more than one occurence of ::)
2. ipv4 mapped ipv6 address - ::ffff:192.168.1.1