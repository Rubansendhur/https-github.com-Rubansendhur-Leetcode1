class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        

        low = 0
        high = len(nums)-1

        while low < high:

            mid = (low + high) // 2

            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
                
            elif nums[mid + 1] > nums[mid]:
               low = mid + 1

            else:
               high = mid
        
        return high
        
        

