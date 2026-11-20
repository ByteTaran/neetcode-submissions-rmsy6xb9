class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            j = i - 1 
            temp = nums[i]
            while j > -1 and temp < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp
        
        return nums
