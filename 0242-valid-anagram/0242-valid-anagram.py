class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}

        if len(s) != len(t):
            return False
        
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in t:
            if i in dict1:
                dict1[i] -= 1
            else:
                return False

        for key,value in dict1.items():
            if value != 0:
                return False
            else:
                return True
        
        


        
            

        