#!/bin/python
import os

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    s_len = len(s)
    s_list = list(s)
    dic = [[s_list[0],1]]
    for i in range(1, s_len):
        if s_list[i] == s_list[i-1]:
            dic[len(dic)-1][1] +=1
        else:
            dic.append([s_list[i], 1])
    
    count += dic[0][1] * (dic[0][1]-1)/2
    
    for i in range(1, len(dic)-1):
        count += dic[i][1] * (dic[i][1]-1)/2
        if (dic[i][1] ==1) and (dic[i-1][0] == dic[i+1][0]):
            count += min(dic[i-1][1], dic[i+1][1])
    
    if len(dic) > 1:
        count +=  dic[len(dic)-1][1] * (dic[len(dic)-1][1]-1)/2

    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
