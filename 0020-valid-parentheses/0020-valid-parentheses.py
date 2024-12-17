class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        n = len(s)

        for i in range(0,n):
            if s[i] == '{' or s[i] == '[' or s[i]=='(':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif s[i] == '}' and stack[-1] != '{':
                   return False
                elif s[i] == ']' and stack[-1] != '[' :
                    return False
                elif s[i] == ')' and stack[-1] != '(':
                    return False
                stack.pop()

        if len(stack) == 0:
                return True
        else:
                return False
            




                
        
        