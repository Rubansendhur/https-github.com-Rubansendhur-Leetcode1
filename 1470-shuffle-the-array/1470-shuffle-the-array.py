class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        res = []

        i = 0
        j = n

        while i < n and j <= len(nums) :
            if len(nums) % 2 == 0:
                res.append(nums[i])
                res.append(nums[j])
                
                i += 1
                j += 1

        return res
            

