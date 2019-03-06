#!/bin/python
import os

def commonChild(s1, s2):
    m = len(s1) 
    n = len(s2) 
    L = [[None]*(n+1) for i in xrange(m+1)] 

    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                if(L[i-1][j] > L[i][j-1]):
                    L[i][j] = L[i-1][j]
                else:
                    L[i][j] = L[i][j-1]
  
    return L[m][n] 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = raw_input()

    s2 = raw_input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
