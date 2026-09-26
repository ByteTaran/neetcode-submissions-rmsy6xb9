class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = list()
        for i in range(len(strs[0])):
            for string in strs:
                if i >= len(string) or strs[0][i] != string[i]:
                    return "".join(ans)

            ans.append(strs[0][i])
        return "".join(ans)