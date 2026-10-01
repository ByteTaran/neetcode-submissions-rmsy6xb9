class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums: List[int], start: int, end: int):
            if start == end:
                return
            mid = (start + end) // 2
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, mid, end)
        
        def merge(nums: List[int], start: int, mid: int, end: int):
            left = start
            right = mid + 1
            temp = list()
            while left <= mid and right <= end:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left <= mid:
                temp.append(nums[left])
                left += 1
            
            while right <= end:
                temp.append(nums[right])
                right += 1
            
            for i in range(len(temp)):
                nums[start + i] = temp[i]
            
        mergeSort(nums, 0, len(nums) - 1)
        return nums

