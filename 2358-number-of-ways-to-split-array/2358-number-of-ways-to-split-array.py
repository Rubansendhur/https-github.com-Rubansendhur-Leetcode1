class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        total = sum(nums)  
        prev = 0    
        for i in range(len(nums)-1):
            prev += nums[i]
            if prev >= total - prev:
               count += 1
        return count
        
        