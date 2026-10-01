class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        isSwap = False
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    isSwap = True
            if not isSwap:
                return nums
        return nums