class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        isSeen = dict()

        for i in range(len(nums)):
            if nums[i] in isSeen and i - isSeen[nums[i]] <= k:
                return True
            isSeen[nums[i]] = i
        return False