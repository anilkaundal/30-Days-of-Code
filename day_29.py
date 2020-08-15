#!/bin/python3

import math
import os
import random
import re
import sys

idlist = []

def findre(emailID):
    x = re.search("^.*@gmail.com$", emailID)
    if x:
        return True
    else:
        return False

if __name__ == '__main__':
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        li = findre(emailID)

        if li is True:
            idlist.append(firstName)

    idlist.sort()

    for i in idlist:
        print(i)
