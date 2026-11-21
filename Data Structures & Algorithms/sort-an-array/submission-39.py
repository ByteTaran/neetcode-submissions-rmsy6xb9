class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            minIndex = i
            for j in range(i + 1, len(nums)):
                if nums[minIndex] > nums[j]:
                    minIndex = j
            nums[minIndex], nums[i] = nums[i], nums[minIndex]
        
        return nums