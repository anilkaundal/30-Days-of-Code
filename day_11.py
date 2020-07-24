#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    '''
    convert integer to binary representation bin(num)
    strips 0b from the binary representation bin(num)[:2]
    split the string on character 0 bin(num)[2:].split('0')
    find the string that has the maximum length and return the number
    '''
    one = max(map(len, bin(n)[2:].split('0')))

    print(one)
