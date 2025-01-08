class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        count = 0
        n=len(words)
        for i in range(0,n):
            word=words[i]
            k=len(word)
            for j in range(i+1,n):
                second_word=words[j]
                print(second_word[len(second_word) -k:])
                if word == second_word[0:k] and word==second_word[len(second_word) -k:]:
                    count+=1
                    
        return count   
                         