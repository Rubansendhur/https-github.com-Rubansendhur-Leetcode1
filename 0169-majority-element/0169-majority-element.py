class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}

        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        threshold = len(nums) / 2

        for key, value in h.items():
            if value > threshold:
                return key
        
        
        