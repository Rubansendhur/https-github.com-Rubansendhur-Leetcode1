class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == '[':
                stack.append(s[i])
            elif s[i] == '{':
                stack.append(s[i])

            else:
                if not stack :
                    return False
                if s[i] == ')' and stack[-1] == '(':
                        stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                        stack.pop()
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False        

        if len(stack) == 0:
            return True
        else:
            return False
            
                
        
        