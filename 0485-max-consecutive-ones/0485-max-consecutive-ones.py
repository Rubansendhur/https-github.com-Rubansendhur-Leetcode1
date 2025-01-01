class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_cons = 0
        count = 0
        i = 0

        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else:
                max_cons = max(max_cons, count)
                count = 0
            i += 1

        max_cons = max(max_cons, count)

            
        return max_cons

        