class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chFreqS = dict()
        chFreqT = dict()


        for ch in s:
            chFreqS[ch] = chFreqS.get(ch, 0) + 1

        for ch in t:
            chFreqT[ch] = chFreqT.get(ch, 0) + 1
        
        
        return chFreqS == chFreqT