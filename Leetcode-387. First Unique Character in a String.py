from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        for char in s:
            if count[char] == 1:
                return s.index(char)
        return -1