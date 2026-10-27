class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = right = 0
        isSeen = set()
        while right < len(nums): 
            if right - left > k:
                isSeen.remove(nums[left])
                left += 1
            if nums[right] in isSeen:
                    return True
                
            isSeen.add(nums[right])
            right += 1
        
        return False