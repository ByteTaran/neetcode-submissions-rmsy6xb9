class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numFreq = dict()

        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        
        numsLen = len(nums)
        res = list()
        for key, val in numFreq.items():
            if val > numsLen // 3:
                res.append(key)
        
        return res