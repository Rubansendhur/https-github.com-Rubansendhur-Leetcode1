class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """

        count = 0
        l = len(pref)
        for i in range(len(words)):
            if words[i][:l] == pref:
                count += 1
        
        return count

        


        