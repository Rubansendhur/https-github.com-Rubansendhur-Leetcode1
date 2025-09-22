class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        max_freq = max(freq.values())
        total = 0

        for k , v in freq.items():
           if v == max_freq:
            total += v
        
        return total
