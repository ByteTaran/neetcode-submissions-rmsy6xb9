class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        minDiff = False
        isSeen = dict()

        for i in range(len(nums)):
            if nums[i] in isSeen:
                minDiff = i - isSeen[nums[i]]
            isSeen[nums[i]] = i
        
        if not minDiff:
            return minDiff
        
        return minDiff <= k
