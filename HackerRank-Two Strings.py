#!/bin/python

import os

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    if len(s1) > len(s2):
        list1 = set(s1)
        list2 = set(s2)
    else:
        list1 = set(s2)
        list2 = set(s1)
    for i in list2:
        if i in list1:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
