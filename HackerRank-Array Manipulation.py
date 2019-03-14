#!/bin/python
# ideas from @amansbhandari
import os

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    ans = [0]*n
    for i in range(len(queries)):
        num = queries[i][2]
        ans[queries[i][0]-1]+= num
        if queries[i][1] < n:
            ans[queries[i][1]] -= num
    x, largest = 0, 0
    for i in range (n):
        x += ans[i]
        if(x> largest):
            largest = x
    return largest



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = raw_input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
