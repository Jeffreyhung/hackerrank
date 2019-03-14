import string
from collections import OrderedDict

# list of all alphabets
alphabets = list(string.ascii_uppercase)

# get the sequence of a list after sorting it
def getSequnce(data):
    data_sorted = sorted(data)
    seq = []
    for i in data:
        seq.append(data_sorted.index(i) - data.index(i))
    return seq

n = int(input())
for _ in range (n):
    keyword = raw_input()
    kw_list = list(OrderedDict.fromkeys(keyword))
    kw_len = len(kw_list)
    sequence = getSequnce(kw_list)
    key1 = []
    key1.append(kw_list)
    tem = []

    for i in alphabets:
        if i not in kw_list:
            if len(tem) == kw_len:
                key1.append(tem)
                del tem
                tem = []
                tem.append(i)
            else:
                tem.append(i)
    tem = tem + ['']*(kw_len - len(tem))
    key1.append(tem)

    key2 = []
    for i in key1:
        tem = [None] * kw_len
        for j in range (kw_len):
            num = ((j+sequence[j])+kw_len)%kw_len
            tem[num] = i[j]
        key2.append(tem)

    key = []
    for i in range (kw_len):
        for j in key2:
            if j[i] !='':
                key.append(j[i])
    
    cipher = raw_input()
    cp_list = list(cipher)
    ans = ''
    for i in cp_list:
        if i == ' ':
            ans += " "
        else:
            tem = key.index(i)
            ans+= chr(tem+65)

    print ans
