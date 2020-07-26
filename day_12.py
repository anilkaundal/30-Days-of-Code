#!/bin/python3

import math
import os
import random
import re
import sys

def max_value(matrix, a, b):
    total = matrix[a][b] 
    total += matrix[a][b + 1]
    total += matrix[a][b + 2] 
    total += matrix[a + 1][b + 1]
    total += matrix[a + 2][b]
    total += matrix[a + 2][b + 1]
    total += matrix[a + 2][b + 2]
    return total

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maximum = -9*7

    for i in range(6):
        for j in range(6):
            if j + 2 < 6 and i + 2 < 6:
                result = max_value(arr, i, j)
                if result > maximum:
                    maximum = result
    print(maximum)
