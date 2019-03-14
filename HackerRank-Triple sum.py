#!/bin/python
import os

def triplets(a, b, c):
    count = 0
    a, b, c = list(sorted(set(a))), list(sorted(set(b))), list(sorted(set(c)))
    a_len, c_len, bi = 0, 0, 0
    while bi < len(b):
        while a_len < len(a) and a[a_len] <= b[bi]:
            a_len += 1
        
        while c_len < len(c) and c[c_len] <= b[bi]:
            c_len += 1
        
        count += a_len * c_len
        bi += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = raw_input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = map(int, raw_input().rstrip().split())

    arrb = map(int, raw_input().rstrip().split())

    arrc = map(int, raw_input().rstrip().split())

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
