class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        minNum = 1
        for num in nums:
            if minNum == num:
                minNum += 1
        return minNum