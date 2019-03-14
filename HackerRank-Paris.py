#!/bin/python

import os

# Complete the pairs function below.
def pairs(k, arr):
    count = 0
    # arr.sort(reverse=True)
    arr_set = set(arr)
    for i in arr_set:
        if i > k:
            if i-k in arr_set:
                count += 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = map(int, raw_input().rstrip().split())

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
