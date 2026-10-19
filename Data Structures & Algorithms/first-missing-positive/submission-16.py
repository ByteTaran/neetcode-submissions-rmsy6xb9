class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        minInteger = 1

        for i in range(len(nums)):
            if nums[i] > 0:
                if nums[i] == minInteger:
                    minInteger += 1
                elif i > 0 and nums[i] == nums[i - 1]:
                    continue
                else:
                    return minInteger
        
        return minInteger
            
                