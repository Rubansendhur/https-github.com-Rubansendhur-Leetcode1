class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = {}

        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1

        for i, j in ans.items():
            if j == 1:
               return i 

        

        

        