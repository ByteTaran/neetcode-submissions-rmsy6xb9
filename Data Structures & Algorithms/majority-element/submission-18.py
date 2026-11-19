class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majEle = None
        countFreq = 0

        for num in nums:
            if countFreq == 0:
                majEle = num
                countFreq += 1
            elif num == majEle:
                countFreq += 1
            else:
                countFreq -= 1
        return majEle