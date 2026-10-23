class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq = dict()

        for num in nums:
            countFreq[num] = countFreq.get(num, 0) + 1
        
        freqList = list()
        
        for num, freq in countFreq.items():
            freqList.append([freq,num])
        
        freqList.sort(reverse=True)
        res = list()

        i = 0
        while len(res) != k:
            res.append(freqList[i][1])
            i += 1
        return res