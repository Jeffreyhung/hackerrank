class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def add(s, digits):
            if (len(digits) == 0):
                ans.append(s)
            else:
                for char in dic[int(digits[0])]:
                    add(s+char, digits[1:])
            
        ans = []
        if digits:
            add("", digits)
        return ans        