#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps += 1
        
    if numSwaps == 0:
        break

firstElement = a[0]
lastElement = a[-1]
print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(firstElement))
print("Last Element: "  + str(lastElement))
