class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        #def cal(self, s1, s2):
           # return self.s1 + self.s2 % 10

        def new(s):
            p = 0
            s1 = ''

            while p < len(s) -1:
                s1 += str((int(s[p]) + int(s[p+1])) % 10)
                p += 1
            return s1

        while len(s) > 2:
            s = new(s)

        return s[0] == s[1]