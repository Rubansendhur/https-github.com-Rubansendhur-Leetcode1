class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        e = extraCandies
        result = []
        max_candy = max(candies)
    
        for i in range (len(candies)):
            if candies[i] + e >= max_candy:
                result.append(True)
            else:
                result.append(False)
        
        return result

        