class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        firstPositive = 1
        nums = set(nums)

        while firstPositive in nums:
            firstPositive += 1
        
        return firstPositive
