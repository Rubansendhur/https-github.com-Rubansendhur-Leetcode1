class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict1 = {}
        ans = 0

        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in t:
            if i in dict1 and dict1[i] > 0:
                dict1[i] -= 1
            else:
                ans += 1
            

        return ans

