import textwrap
from collections import OrderedDict

def merge_the_tools(string, k):
    for i in textwrap.wrap(string, k):
        print "".join(OrderedDict.fromkeys(i))

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    