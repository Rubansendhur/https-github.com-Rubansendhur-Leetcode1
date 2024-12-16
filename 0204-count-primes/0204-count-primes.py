class Solution:
    def countPrimes(self, n: int) -> int:
        prime = []
        if( n <= 1):
            return 0
            
        prime = [1] * n
        prime[0] = 0
        prime[1] = 0

        ans = 0

        for i in range(2,n):
            if prime[i] == 1:
                for j in range(2*i, n , i):
                    prime[j] = 0
        
        for i in prime:
            if i == 1:
                ans +=1
        
        return ans