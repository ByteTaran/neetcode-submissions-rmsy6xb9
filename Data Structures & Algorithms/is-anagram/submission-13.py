class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chInS = dict()
        chInT = dict()
        for ch in s:
            chInS[ch] = chInS.get(ch, 0) + 1

        for ch in t:
            chInT[ch] = chInT.get(ch, 0) + 1
        
        return chInT == chInS