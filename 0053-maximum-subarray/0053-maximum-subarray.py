class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        end_no = nums[0]
        res = nums[0]
        temp = 0
        
        for i in range(1,len(nums)):
            end_no = max(end_no + nums[i], nums[i])
            res = max(end_no , res)

        return res
            




        