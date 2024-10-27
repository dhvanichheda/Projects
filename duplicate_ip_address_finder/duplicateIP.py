#!/usr/bin/env python3

import sys
from pathlib import Path
from typing import List, Dict

def find_duplicate_IPs(log_IPs: List[str]) -> Dict[str, int]:
    ip_map = {}
    for ip in log_IPs:
        ip_map[ip] = ip_map.get(ip, 0) + 1
    return {ip: count for ip, count in ip_map.items() if count > 1}

if __name__ == '__main__':
    input_file_path = input('Enter the path of your log file containing IP addresses')
    path_obj = Path(input_file_path)
    if not path_obj.is_file():
        sys.exit("Invalid input file path")

    log_IPs = []
    with open(input_file_path, 'r') as f:
        for line in f:
            log_IPs.append(line.strip())

    duplicates = find_duplicate_IPs(log_IPs)
    print(f'duplicates - {duplicates}')