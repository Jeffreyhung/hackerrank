#!/bin/python
import os

def minimumSwaps(arr, n):
    count = 0
    for i in range (n-1):
        if arr[i] != i+1:
            temp = arr.index(i+1, i)
            arr[i], arr[temp] =arr[temp], arr[i]
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(raw_input())
    arr = map(int, raw_input().rstrip().split())
    res = minimumSwaps(arr, n)
    fptr.write(str(res) + '\n')
    fptr.close()
