def isValid(s):
    stack = []
    dict = {')':'(', ']':'[','}':'{'}

    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        tem = ""
        if (n==1):
            return ["()"]
        for i in range (pow(2, 2*(n-1))):
            tem += "("
            num = str('{:b}'.format(i)).zfill(2*(n-1))
            for char in num:
                if(char == '0'):
                    tem+="("
                else:
                    tem+=")"
            tem += ")"
            if isValid(tem):
                ans.append(tem)
            tem = ""
        return ans
            
        