class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        exact = set(wordlist)
        case_track = {}
        vowel_track = {}

        for w in wordlist:
            lower = w.lower()
            devowel = self.devowel(lower)

            if lower not in case_track:
                case_track[lower] = w
            if devowel not in vowel_track:
                vowel_track[devowel] = w

        res = []

        for q in queries:
            if q in exact:
                res.append(q)
            else:
                lower = q.lower()
                devowel = self.devowel(lower)
                if lower in case_track:
                    res.append(case_track[lower])
                elif devowel in vowel_track:
                    res.append(vowel_track[devowel])
                else:
                    res.append("")
        
        return res
        

    def devowel(self, s):
            return ''.join('*' if c in 'aeiou' else c for c in s)
        
