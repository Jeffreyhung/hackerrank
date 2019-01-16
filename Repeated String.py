#!/bin/python

import os

# Complete the repeatedString function below.
def repeatedString(s, n):
    count=0
    num_of_a = s.count('a')
    rounds = n/len(s)
    remains = n % len(s)
    remains_num_of_a = 0
    if remains != 0:
        rest = s[:remains]
        remains_num_of_a = rest.count('a')
    count = num_of_a * rounds + remains_num_of_a
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
