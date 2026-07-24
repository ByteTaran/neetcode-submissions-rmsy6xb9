class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majEle = None
        majFreq = 0
        for num in nums:
            if not majFreq:
                majEle = num
                majFreq += 1
            elif majEle == num:
                majFreq += 1
            else:
                majFreq -= 1
        return majEle