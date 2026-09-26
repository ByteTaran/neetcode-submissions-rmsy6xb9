from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            chCount = [0] * 26
            for ch in string:
                chCount[ord(ch) - ord("a")] += 1
            anagrams[tuple(chCount)].append(string)

        return list(anagrams.values())
