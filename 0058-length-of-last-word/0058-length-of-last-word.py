class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = 0
        found = False
        for i in range(len(s) -1, -1, -1):
            if s[i] != ' ':
                length += 1
                found = True
            elif found:
                break
        
        return length


               
        

