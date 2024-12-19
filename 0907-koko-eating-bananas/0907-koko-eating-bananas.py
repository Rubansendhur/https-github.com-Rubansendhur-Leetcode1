class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        fin = 0

        while i <= j:
            k = (i+j) // 2
            temp = 0

            for x in range(0,len(piles)):
                temp = temp + ceil(piles[x] / k)
            if(temp <= h):
                fin = k
                j = k - 1
            else:
                i = k + 1

        return fin

        