class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        minInteger = 1

        while minInteger in nums:
            minInteger += 1
        
        return minInteger