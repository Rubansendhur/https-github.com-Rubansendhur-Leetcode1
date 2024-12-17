class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []

        for i in range(len(s)):
            if s[i] != '#':
                s1.append(s[i])
            else:
                if (len(s1) != 0):
                    s1.pop()

        for i in range(len(t)):
            if t[i] != '#':
                s2.append(t[i])
            else:
                if (len(s2) != 0):
                    s2.pop()
        
        if s1 == s2:
            return True
        else:
            return False