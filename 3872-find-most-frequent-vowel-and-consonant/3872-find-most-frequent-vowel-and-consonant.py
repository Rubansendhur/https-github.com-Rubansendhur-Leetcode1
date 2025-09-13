class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq_tab = {}

        for i in s:
            if i not in freq_tab:
                freq_tab[i] = 1
            else:
                freq_tab[i] += 1
        
        vow_count, const_count = 0 , 0

        for key,value in freq_tab.items():
            if key in "aeiou":
                vow_count = max(vow_count, value)
            else:
                const_count = max(const_count, value)
        
        return vow_count + const_count
            
                