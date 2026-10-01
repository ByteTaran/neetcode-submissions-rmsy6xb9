class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i > -1 and s[i] == ' ':
            i -= 1
        
        j = i
        
        while i > -1 and s[i] != ' ':
            i -= 1

        return j - i