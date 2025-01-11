class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """

        r = 0

        if len(s) < k:
            return False

        if len(s) == k:
            return True

        arr = [0] * 26

        for ch in s:
            arr[ord(ch) - ord('a')] += 1

        oddCharCnt = sum(1 for count in arr if count % 2 == 1)

        return oddCharCnt <= k
        