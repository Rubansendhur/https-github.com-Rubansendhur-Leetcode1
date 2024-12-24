class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #find Duplicates
        h = {}

        for i in range(len(nums)):
            if nums[i] in h:
                if abs(h[nums[i]] - i) <= k:
                    return True
            h[nums[i]] = i
        
        return False
                    