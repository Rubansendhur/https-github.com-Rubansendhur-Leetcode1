class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        s = []
        A , B = len(word1), len(word2)
        a , b = 0 , 0

        word = 1

        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            
            if word == 2:
                s.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            s.append(word1[a])
            a += 1

        while b < B:
            s.append(word2[b])
            b += 1

        return ''.join(s)
     


        