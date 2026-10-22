class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for num in nums:
            index = abs(num) - 1
            if -1 < index < len(nums):
                if 0 < nums[index]:
                    nums[index] *= -1
                elif 0 == nums[index]:
                    nums[index] = -1 * (len(nums) + 1)
        
        for i in range(len(nums)):
            if nums[i] > -1:
                return i + 1
        
        return len(nums) + 1