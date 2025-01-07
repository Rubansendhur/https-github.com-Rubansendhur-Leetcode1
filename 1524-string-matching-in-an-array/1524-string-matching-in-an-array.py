class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(0,len(words)):
            for j in words:
                if words[i] in j and words[i] != j:
                    if words[i] not in ans:
                        ans.append(words[i])
        return ans
        