class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = list()
        for word in strs:
            encode.append(str(len(word)) + "#" + word)
        return "".join(encode)

    def decode(self, s: str) -> List[str]:
        decode = list()
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordLen = int(s[i:j])
            decode.append(s[j + 1:j + wordLen + 1])
            i = j + wordLen + 1
        
        return decode