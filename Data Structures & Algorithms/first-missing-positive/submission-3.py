class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numsLen = len(nums)
        for i in range(numsLen):
            if nums[i] < 0:
                nums[i] = 0
        
        for num in nums:
            val = abs(num)
            if 1 <= val <= numsLen:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = (numsLen + 1) * -1
        
        for i in range(numsLen):
            if nums[i] >= 0:
                return i + 1
        
        return numsLen + 1