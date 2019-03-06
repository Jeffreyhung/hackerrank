#!/bin/python

import os
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    s_counter = Counter(s)
    counter2 = Counter(s_counter.values())
    max_item = counter2.most_common(3)
    print max_item
    if(len(max_item)<2):
        return "YES"
    elif (len(max_item) == 3):
        return "NO"
    elif ( max_item[1][0] == 1) and (max_item[1][1] == 1):
        return "YES"
    elif (max_item[1][1] < 2) and (abs(max_item[1][0]-max_item[0][0])<2) :
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
