#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    dictionary = s.split(" ")
    result = ""    
    for i in dictionary:
        if i == "":
            result += " "
        else:
            temp = list(i)
            if(ord(temp[0])>96) and (ord(temp[0])<123):
                temp[0] =chr(ord(temp[0])-32)
            result += ''.join(temp) + " "
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
