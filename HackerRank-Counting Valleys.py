#!/bin/python

import os

# Complete the countingValleys function below.
def countingValleys(n, s):
    count =0
    previous=0
    valleys = 0
    info = list(s)
    for i in range(n):
        previous = count
        if info[i] == 'U':
            count+=1
        else:
            count-=1
        if (previous < 0) and (count == 0):
            valleys+=1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
