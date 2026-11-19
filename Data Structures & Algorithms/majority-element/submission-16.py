class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numFreq = dict()
        majElement = None
        maxFreq = 0
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        
        for num, freq in numFreq.items():
            if freq > maxFreq:
                maxFreq = freq
                majElement = num
        return majElement