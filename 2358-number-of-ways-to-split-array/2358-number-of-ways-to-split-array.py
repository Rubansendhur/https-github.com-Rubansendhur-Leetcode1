class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        total = sum(nums)  
        pref = 0    

        for i in range(len(nums)-1):
            pref += nums[i]
            if pref >= total - pref:
               count += 1
        return count
        
        