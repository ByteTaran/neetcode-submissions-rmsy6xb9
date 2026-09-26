class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majEle = nums[0]
        freq = 0

        for num in nums:
            if freq == 0:
                majEle = num
                freq = 1
            elif num == majEle:
                freq += 1
            elif num != majEle:
                freq -= 1

        return majEle