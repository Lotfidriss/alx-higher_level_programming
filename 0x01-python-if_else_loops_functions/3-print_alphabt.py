#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    if i != ord('q') or i != ord('e'):
     print("{:c}".format(i), end="")
