class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ""  # To store the longest palindromic substring
        temp = ""  # Temporary substring to check for palindrome

        if len(s) == 1:
            return s  # If the string has only one character, it's the longest palindrome

        for i in range(len(s)):
            for j in range(i, len(s)):  # Generate substrings dynamically
                temp = s[i:j+1]  # Extract substring from index i to j
                
                if longest == "":  # If no palindrome found yet, store the first one
                    longest = temp

                if temp == temp[::-1]:  # Check if the substring is a palindrome
                    if len(temp) > len(longest):  # Update longest if temp is longer
                        longest = temp
        
        return longest
            
        