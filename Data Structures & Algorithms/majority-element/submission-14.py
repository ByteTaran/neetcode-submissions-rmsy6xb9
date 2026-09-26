class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numFreq = dict()

        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        
        for num, freq in numFreq.items():
            if freq > len(nums) // 2:
                return num
                