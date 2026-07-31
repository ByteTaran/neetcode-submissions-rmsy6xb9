class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        
        numsLen = len(nums)
        numFreq = dict()

        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        res = list()
        for key, value in numFreq.items():
            if value > numsLen // 3:
                res.append(key)
        
        return res