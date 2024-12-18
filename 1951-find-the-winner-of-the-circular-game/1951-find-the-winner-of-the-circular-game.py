class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        c = 1
        q = []

        for i in range(1 , n+1):
            q.append(i)

        while len(q) > 1:
            a = q.pop(0)
            if c != k:
                q.append(a)
                c += 1
            else:
                c = 1

        return q[0]


        