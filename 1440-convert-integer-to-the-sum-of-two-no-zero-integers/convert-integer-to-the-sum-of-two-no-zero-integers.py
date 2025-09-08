class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        res = []
        for i in range(1, n//2 +1):
            a = str(i)
            b = str(n - i)
            if '0' not in a and '0' not in b:
                res.append(int(a))
                res.append(int(b))
                return res


    
                


