class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = maxLength = 0
        trackLastIndex = dict()

        for right in range(len(s)):
            if s[right] in trackLastIndex:
                left = max(trackLastIndex[s[right]] + 1, left)
            trackLastIndex[s[right]] = right
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength