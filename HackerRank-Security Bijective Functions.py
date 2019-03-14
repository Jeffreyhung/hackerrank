import fileinput
data =[]
for line in fileinput.input():
    data.append(line)

data2 = data[1].split(" ")



if len(set(data2)) == len(data2):
    print "YES"
else:
    print "NO"
