class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trackIndex = dict()
        for i in range(len(nums)):
            if target - nums[i] in trackIndex:
                return [trackIndex[target - nums[i]], i]
            trackIndex[nums[i]] = i