class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = dict()

        for num in nums:
            numFreq[num] = numFreq.get(num,0) + 1


        bucket = [[] for _ in range((len(nums) + 1))]
        for num, freq in numFreq.items():
            bucket[freq].append(num)
        res = list()       
        
        for i in range(len(bucket) - 1, -1, -1):
            for j in range(len(bucket[i]) - 1, -1, -1):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res
                
