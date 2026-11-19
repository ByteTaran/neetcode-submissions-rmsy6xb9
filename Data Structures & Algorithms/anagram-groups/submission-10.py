from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            bucket = [0] * 26
            for ch in string:
                bucket[ord(ch) - ord("a")] += 1
            res[tuple(bucket)].append(string)
        
        return list(res.values())
