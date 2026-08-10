class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = list()
        countFreq = dict()
        ans = list()
        for num in nums:
            countFreq[num] = countFreq.get(num, 0) + 1
        
        for num, val in countFreq.items():
            freqList.append([val, num])
        
        freqList.sort(reverse=True)

        while len(ans) < k:
            ans.append(freqList[len(ans)][1])
        
        return ans