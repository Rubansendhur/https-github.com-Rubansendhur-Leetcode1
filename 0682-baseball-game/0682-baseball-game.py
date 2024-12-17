class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ch = operations
        n = len(ch)

        for i in range(n):
            if ch[i] == 'C':
                stack.pop()
            elif ch[i] == 'D':
                stack.append(stack[-1] * 2)
            elif ch[i] == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(ch[i]))
        sum = 0
        while len(stack) > 0:
            sum += stack.pop()
            
        return sum
        