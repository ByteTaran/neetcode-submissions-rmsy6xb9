class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        minDiff = None
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if not minDiff:
                        minDiff = j - i
                    else:
                        minDiff = min(j - i, minDiff)
        if not minDiff:
            return False
        return minDiff <= k       
        
