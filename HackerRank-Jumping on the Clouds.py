#!/bin/python

import os

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c):
    step =0
    location=0
    for i in range(n):
        if (n-location)>2:
            if c[location+2] != 1:
                step+=1
                location+=2
            else:
                step+=1
                location +=1
        else:
            step+=1
            location +=1
        if location ==(n-1):
            return step


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(n,c)

    fptr.write(str(result) + '\n')

    fptr.close()
