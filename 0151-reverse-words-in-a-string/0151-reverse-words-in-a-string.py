class Solution:
    def reverseWords(self, s: str) -> str:

        i = len(s) -1
        j = len(s) -1
        words = []

        while i >= 0:
            if s[i] == ' ':
                if i < j:
                    words.append(s[i + 1:j + 1]) 
                j = i - 1 
            i -= 1

        if i < j:
            words.append(s[i + 1:j + 1])

        return ' '.join(words)

            
                 
        

        