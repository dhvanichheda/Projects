# IP Address Parser

Basic Python project to parse valid IP addresses from a file containing values per line.

## Table of Contents

1. [Overview](#overview)
2. [Types of IP Addresses](#types-of-ip-addresses)
3. [IPv4 Address Format](#ipv4-address-format)
4. [IPv6 Address Format](#ipv6-address-format)
5. [Edge Cases](#edge-cases)

## Overview

This project identifies valid IP addresses from a file, distinguishing between IPv4 and IPv6 formats. It checks the validity of the addresses based on defined conditions.

## Types of IP Addresses

There are 2 types of IP addresses:

1. **IPv4**
2. **IPv6**

## IPv4 Address Format

### Format

A valid IPv4 address follows the format `0.0.0.0`.

### Conditions for Validity

1. Contains 4 integers separated by periods.
2. Each integer must have a value between 0 and 255.

## IPv6 Address Format

### Format

A valid IPv6 address follows the format `x:x:x:x:x:x:x:x`.

### Conditions for Validity

1. Contains 8 hex values (16 bits each) separated by colons.
2. Each hex value can range between `0000` to `ffff`.

## Edge Cases

- **Compressed IPv6**: Example: `2001:db8::1` (There cannot be more than one occurrence of `::`.)
- **IPv4 Mapped IPv6 Address**: Example: `::ffff:192.168.1.1`.
