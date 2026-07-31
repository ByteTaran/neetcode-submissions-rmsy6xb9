class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        numCount = 0
        numsLen = len(nums)
        prevNum = nums[0]
        res = list()
        for num in nums:
            if num == prevNum:
                numCount += 1
            else:
                if numCount > numsLen // 3:
                    res.append(prevNum)
                prevNum = num
                numCount = 1
        if numCount > numsLen // 3:
            res.append(prevNum)
        return res