#!/bin/python


import os

# Complete the rotLeft function below.
def rotLeft(a, d,n):
    copy = a[:]
    for i in range(len(a)):
        print (i+d)%n
        a[i] = copy[(i+d)%n]
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d,n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
