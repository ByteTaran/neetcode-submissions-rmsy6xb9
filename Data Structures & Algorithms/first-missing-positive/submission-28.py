class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        minNum = 1

        for num in nums:
            if num < 1 or num == minNum - 1:
                continue
            elif minNum < num:
                return minNum
            minNum += 1
            

        return minNum
            