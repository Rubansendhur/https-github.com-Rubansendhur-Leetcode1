class Solution:
    def findMin(self, nums: List[int]) -> int:

        ans = sorted(nums)
        return ans[0]

        