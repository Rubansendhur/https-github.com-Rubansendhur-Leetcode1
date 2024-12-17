class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)

        for i in range(n):
            if tokens[i] == '/' :
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            elif tokens[i] == '+' :
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif tokens[i] == '*' :
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif tokens[i] == '-' :
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            else:
                stack.append(int(tokens[i]))
        
        return stack.pop()
            

        

        