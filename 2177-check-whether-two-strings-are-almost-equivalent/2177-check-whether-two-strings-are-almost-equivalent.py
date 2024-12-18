class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        dict1 = {}
        ans = 0
        s=word1
        t=word2
        
        if len(s) != len(t):
            return False
        
        for i in s:
            if i in dict1 and dict1[i] > 0:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in t:
            if i in dict1:
                dict1[i] -= 1
            else:
                dict1[i] = -1

        print(dict1)

        for value in dict1.values():
            if abs(value) > 3:
                return False
           
        return True
            
       

        