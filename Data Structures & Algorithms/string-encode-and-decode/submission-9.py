class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = list()
        for string in strs:
            encodedString.append(str(len(string)) + "#" + string)
        
        return "".join(encodedString)

    def decode(self, s: str) -> List[str]:
        i = 0
        decodedString = list()
        while i < len(s):
            j = i
            wordLen = list()
            while s[j].isalnum():
                wordLen.append(s[j])
                j += 1
            decodedString.append(s[j + 1:j + int("".join(wordLen)) + 1])
            i = j + int("".join(wordLen)) + 1
        
        return decodedString