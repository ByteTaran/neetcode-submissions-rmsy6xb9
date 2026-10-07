class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numFreq = dict()

        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        
        res = list()
        for num, freq in numFreq.items():
            if freq > len(nums) // 3:
                res.append(num)
        
        return res