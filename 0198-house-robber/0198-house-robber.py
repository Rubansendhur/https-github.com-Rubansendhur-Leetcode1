class Solution:

    def dp(self, i , nums,dp):
        if(i < 0):
            return 0
        if(dp[i]!= -1):
            return dp[i]
        a1 = nums[i] + self.dp(i-2, nums, dp)
        a2 = self.dp(i-1, nums, dp)
        dp[i] = max(a1, a2)
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        dp = [-1] *len(nums)
        return self.dp(len(nums)-1,nums,dp)

        


        
        