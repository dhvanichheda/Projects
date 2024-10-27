Given a list of IP addresses from log files, identify any duplicate IPs and count their occurrences.

Reference input and output - 

Input:
log_ips = [
    "192.168.1.1",
    "10.0.0.1",
    "192.168.1.1",
    "172.16.0.1",
    "10.0.0.1",
    "192.168.1.1",
    "192.168.1.2"
]

Output:
{
    "192.168.1.1": 3,
    "10.0.0.1": 2
}