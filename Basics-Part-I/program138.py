'Write a Python program to valid an IP address.'

import socket

addr = input('Enter an IP address ')
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")
	