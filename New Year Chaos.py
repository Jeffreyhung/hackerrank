#!/bin/python

# Complete the minimumBribes function below.
def minimumBribes(q,n):
    count = 0
    for i in range(len(q)-1,-1,-1):
        if (q[i]-(i+1)>2):
            return "Too chaotic"
        for j in range(max(0,q[i]-2),i,+1):
            if q[j] > q[i]:
                count+=1
    return count


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        print minimumBribes(q, n)
