class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq = dict()
        for num in nums:
            countFreq[num] = countFreq.get(num, 0) + 1
        
        freqBucket = [[] for _ in range((len(nums) + 1))]
        for num, freq in countFreq.items():
            freqBucket[freq].append(num)
        
        ans = list()
        for i in range(len(freqBucket) - 1, -1, -1):
            for val in freqBucket[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans
        return ans
                
            