#!/bin/python

import os

def matching(target, others):
    for i in range (len(others)):
        if target == others[i]:
            return True
    return False

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    paired = 0
    left = ar
    single=[]
    for i in range(len(ar)):
        if left:
            tem = left[0]
            del left[0]
            if matching(tem, left):
                paired+=1
                left.remove(tem)
            else:
                single.append(tem)
    return paired

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
