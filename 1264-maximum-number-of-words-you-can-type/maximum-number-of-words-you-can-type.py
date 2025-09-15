class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        res = 0
        broken = set(brokenLetters)
        words = text.split()

        for word in words:
            if all(ch not in broken for ch in word):
                res += 1
        return res
            