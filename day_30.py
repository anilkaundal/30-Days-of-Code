#!/bin/python3

import math
import os
import random
import re
import sys

def bitwiseand(n, k):
    maximum = 0
    for i in range(1, n+1):
            for j in range(1, i):
                l = i & j
                if maximum<l<k:
                    maximum = l
                    if maximum == k-1:
                        return maximum
    
    return maximum

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(bitwiseand(n, k))
