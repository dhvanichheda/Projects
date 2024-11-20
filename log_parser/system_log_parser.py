#!/usr/bin/env python3

'''
1. Input - info, warn or error or i, w, e
'''

import sys
from pathlib import Path

def validate_log_level(log_level: str) -> [bool, str]:
    valid = {
        "info": "INFO",
        "i": "INFO",
        "error": "ERROR",
        "e": "ERROR",
        "warn": "WARN",
        "w": "WARN"
    }

    log_level = log_level.strip().lower()
    if log_level in valid:
        return True, valid[log_level]
    else:
        return False, "Invalid input. Valid - info[I], warn[W], error[E]"
    

def parse_logs(log_file: str, log_level: str):
    with open(log_file, 'r') as f:
        for log in f:
            if log_level in log:
                print(log)

if __name__ == "__main__":
    log_file_input = input("Enter the log file path that you want to parse: ")
    log_file_path = Path(log_file_input)
    if not log_file_path.is_file():
        sys.exit("Invalid log file path")

    log_level_input = input("Enter the log level that you want to parse - info[I], warn[W] or error[E]: ")
    valid, log_level = validate_log_level(log_level_input)
    if not valid:
        sys.exit(log_level)

    parse_logs(log_file_path, log_level)

    


