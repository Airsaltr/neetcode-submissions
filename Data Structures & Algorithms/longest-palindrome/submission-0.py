class Solution:
    def longestPalindrome(self, s: str) -> bool:
        char_set = set()
        length = 0
        
        for char in s:
            if char in char_set:
                char_set.remove(char)
                length += 2
            else:
                char_set.add(char)
        return length + 1 if char_set else length
