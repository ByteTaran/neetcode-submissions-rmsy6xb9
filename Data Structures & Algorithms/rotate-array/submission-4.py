class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        while k:
            prevNum = nums[-1]
            for i in range(len(nums)):
                temp = nums[i]
                nums[i] = prevNum
                prevNum = temp

            k -= 1