class Solution:
    def isPalindrome(self, s: str) -> bool:
        cl_lower = s.lower()
        cl = ''.join(char for char in cl_lower if char.isalnum())
        i = 0
        j = len(cl)-1
       
        print(cl)

        while i <= j:
            if cl[i] == cl[j]:
                i += 1
                j -= 1
            else:
                return False

        return True
                


        
        