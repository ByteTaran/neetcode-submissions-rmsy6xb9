class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = list()
        countNum = 0
        currNum = nums[0]
        for num in nums:
            if num == currNum:
                countNum += 1
            else:
                countNum = 1
                currNum = num
            if countNum > len(nums) // 3 and num not in res:
                    res.append(num)
        return res