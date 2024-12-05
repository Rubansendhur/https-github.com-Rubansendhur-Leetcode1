class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

       i = 0
       j = 0
       sub = ''

       while i < len(s) and j < len(t):
        if s[i] == t[j]:
            sub += s[i]
            i += 1
        j += 1

       if sub == s:
        return True
       else:
        return False
    
        
        

       
       
