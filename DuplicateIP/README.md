# Duplicate IP Address Finder

Given a list of IP addresses from log files, this project identifies any duplicate IPs and counts their occurrences.

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Input](#input)
3. [Output](#output)
4. [Installation](#installation)
5. [Usage](#usage)
6. [License](#license)

## Problem Statement

Write a function that takes a list of IP addresses and returns a dictionary with the counts of each unique IP address.

## Input

The function takes the following input:

```python
log_ips = [
    "192.168.1.1",
    "10.0.0.1",
    "192.168.1.1",
    "172.16.0.1",
    "10.0.0.1",
    "192.168.1.1",
    "192.168.1.2"
]

## Output

The function returns a dictionary that counts the occurrences of each IP address:

```python
{
    "192.168.1.1": 3,
    "10.0.0.1": 2
}
