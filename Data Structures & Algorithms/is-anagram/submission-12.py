class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        chCountS = dict()
        chCountT = dict()

        for ch in s:
            chCountS[ch] = chCountS.get(ch, 0) + 1
        
        for ch in t:
            chCountT[ch] = chCountT.get(ch, 0) + 1
        
        return chCountT == chCountS