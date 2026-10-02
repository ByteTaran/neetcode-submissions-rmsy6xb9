class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        numFreq = list()
        if len(nums) == 1:
            return nums

        countFreq = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                countFreq += 1
            else:
                numFreq.append([countFreq, nums[i - 1]])
                countFreq = 1
        
        numFreq.append([countFreq, nums[-1]])
        numFreq.sort(reverse=True)

        res = list()
        for num in range(k):
            res.append(numFreq[num][1])
        
        return res