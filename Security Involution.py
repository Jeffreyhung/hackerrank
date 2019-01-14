n = input()
x = []
x = raw_input().split(" ")

check = 0

for i in range(0, n):
    # print i+1
    # print x[int(x[i])-1]
    if (i+1) == int(x[int(x[i])-1]):
        check+=1
    else:
        check+=0

#print check


if check ==n:
    print "YES"
else:
    print "NO"
