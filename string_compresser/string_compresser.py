#!/usr/bin/env python3
'''
Compress a string like "aaabbbaaa" into a string like "3a3b3c" and print the length of the compressed string
If a character occurs only once, no need to prefix it with a 1 eg. "abbbc" should be "a3bc"
'''

def compress(in_str: str) -> str:
    if not in_str:
        return ""
    curr = in_str[0]
    out_str = ""
    curr_count = 1

    for idx in range(1, len(in_str)):
        if in_str[idx] == curr:
            curr_count += 1
        else:
            out_str += curr if curr_count == 1 else str(curr_count) + curr 
            curr = in_str[idx]
            curr_count = 1

    out_str += curr if curr_count == 1 else str(curr_count) + curr 
    return out_str


if __name__ == "__main__":
    in_str = input("Enter the input string")
    compressed = compress(in_str)
    print(compressed)
    print(len(compressed))