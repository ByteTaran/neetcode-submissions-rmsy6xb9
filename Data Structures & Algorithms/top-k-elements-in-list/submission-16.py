class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = dict()
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        
        freqList = [[] for _ in range(len(nums) + 1)]

        for num, idx in numFreq.items():
            freqList[idx].append(num)
        
        res = list()
        for idx in range(len(freqList) - 1, -1, -1):
            for num in range(len(freqList[idx])):
                if len(res) != k:
                    res.append(freqList[idx][num])
                else:
                    return res
        
        return res
                