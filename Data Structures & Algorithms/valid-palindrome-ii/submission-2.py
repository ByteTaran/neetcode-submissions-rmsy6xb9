class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.checkPalindrome(s, i, j - 1) or self.checkPalindrome(s, i + 1, j)

        return True

    def checkPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True

