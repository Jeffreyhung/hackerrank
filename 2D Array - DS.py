#!/bin/python

import os

# Complete the hourglassSum function below.
def hourglassSum(arr):
    count =  [[0] * 4,[0] * 4,[0] * 4,[0] * 4]
    for i in range(4):
        for j in range(4):
            count[i][j] = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
    return max(map(max, count))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
