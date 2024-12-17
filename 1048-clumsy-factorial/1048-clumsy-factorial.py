class Solution:
    def clumsy(self, n: int) -> int:
        stack = []
        stack.append(n)
        n = n - 1

        c = 0

        while n >= 1:
            if c == 0:
                stack[-1] = stack[-1] * n
                n -= 1
                c += 1
            elif c == 1:
                stack[-1] = int(stack[-1] / n)
                n -= 1
                c += 1
            elif c == 2:
                stack[-1] = (stack[-1] +  n)
                n -= 1
                c += 1
            elif c == 3:
                stack.append(-n)
                n -= 1
                c = 0
                
        return sum(stack)
            
        



        
        