#!/usr/bin/env python3

from pathlib import Path 
import re 
import sys 

#pre-compile the regex for ipv4 and ipv6
ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$') # this regex does not check for the valid range of 0 to 255. We do that check in the function.
ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$') #does not include compressed ipv6 patterns e.g. 1111::2
ipv4_mapped_ipv6_pattern = re.compile(r'^::ffff:(\d{1,3}\.){3}\d{1,3}$')

def checkIfIPv4(line: str) -> bool :
    if not ipv4_pattern.match(line):
        return False
    
    octets = line.split('.')
    return all( 0 <= int(octet) < 256 for octet in octets)

def checkIfIPv6(line: str) -> bool: 
    if ipv6_pattern.match(line):
        return True 
    
    if ipv4_mapped_ipv6_pattern.match(line):
        return True 

    #check for compressed parts 
    ipv6_split = line.split(":")                       
    if len(ipv6_split) > 8:
        return False 
    if line.count('::') > 1:
        return False 
    for part in ipv6_split:
        if part and not (1 <= len(part) <= 4 and all(c in '0123456789abcdefABCDEF' for c in part)):
            return False
        
    return True 
    

if __name__ == "__main__":

    input_file_path = input('Enter the input file path: ')
    print(f'input file path - {input_file_path}')
    path_obj = Path(input_file_path)
    if not path_obj.is_file():
        sys.exit('input file path is invalid')

    #read input file line by line 
    with open(input_file_path, 'r') as f:
        for line in f:
            if checkIfIPv4(line) or checkIfIPv6(line):
                print(line)