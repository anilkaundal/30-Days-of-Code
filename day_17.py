#!/bin/python3

import sys


S = input().strip()
try:
    string = int(S)
    print(string)
except:
    print("Bad String")
