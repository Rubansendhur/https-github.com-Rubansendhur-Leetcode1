class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(cur_per):

            if n == len(cur_per):
                res.append(cur_per.copy())
            
            for num in nums:
                if num in cur_per:
                    continue
                
                cur_per.append(num)
                backtrack(cur_per)
                cur_per.pop()

        backtrack([])
        return res


        