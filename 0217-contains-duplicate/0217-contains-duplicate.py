class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        print(hash)

        for key,val in hash.items():
            if val > 1:
                return True

        return False
        
       
        