class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(start: int, end: int) -> None:
            if start == end:
                return None
            mid = (start + end) // 2
            mergeSort(start, mid)
            mergeSort(mid + 1, end)
            merge(start, mid, end)
        
        def merge(start: int, mid: int, end: int) -> None:
            left = start
            right = mid + 1
            temp = list()
            
            while left <= mid and right <= end:
                if nums[left] < nums[right]:
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
                nums[i + start] = temp[i]

        
        mergeSort(0, len(nums) - 1)
        return nums
