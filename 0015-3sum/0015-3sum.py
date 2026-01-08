class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()

        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         complement = nums[i] + nums[j]
        #         for k in range(j+1, len(nums)):
        #             if complement + nums[k] == 0 and i != j and i != k and j !=k:
        #                 res.add((nums[i], nums[j], nums[k]))

        # return list(res)

        for i in range(len(nums)-2):

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                
                elif total > 0:
                    k -= 1
                
                else:
                    j += 1
                

        return list(res)
        