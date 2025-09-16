class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        import math

        n = len(nums)
        stack = []

        for num in nums:
            while stack and self.gcd(stack[-1], num) > 1:
                num = self.lcm(stack.pop(), num)
            stack.append(num)
        
        return stack

        
    def gcd(self , a , b):
        return math.gcd(a,b)
        
    def lcm(self , a, b):
        return math.lcm(a,b)