class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            ans = ans ^ nums[i]
        return ans
        