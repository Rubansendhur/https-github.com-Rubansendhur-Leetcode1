class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        result = 0

        for i in range(1 , 61):
            target = num1 - i * num2

            if target < i:
                return - 1
            if i >= target.bit_count():
                return i
                result = i
        
        return result