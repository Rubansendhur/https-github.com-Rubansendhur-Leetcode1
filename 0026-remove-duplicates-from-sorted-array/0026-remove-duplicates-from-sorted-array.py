class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        if not a:
            return 0
        
        i = 0
        
        for j in range(1, len(a)):
            if a[j] != a[i]:
                i += 1
                a[i] = a[j]
        
        return i + 1 
        