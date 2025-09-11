class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []

        s_list = list(s)

        print("lists", s_list)

        for i in s_list:
            if i in 'aeiouAEIOU':
                vowels.append(i)
        
        if vowels == []:
            return s
        
        vowels.sort()
        count = 0

        print(vowels)

        for j in range(len(s)):
            if s_list[j] in 'aeiouAEIOU':
                s_list[j] = vowels[count]
                count += 1

        return "".join(s_list)


