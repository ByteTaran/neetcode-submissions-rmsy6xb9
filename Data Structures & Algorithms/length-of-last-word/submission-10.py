class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        i = len(s) - 1
        countLen = 0
        while i > -1 and s[i] == " ":
            i -= 1
        while i > -1 and s[i] != " ":
            countLen += 1
            i -= 1
        
        return countLen