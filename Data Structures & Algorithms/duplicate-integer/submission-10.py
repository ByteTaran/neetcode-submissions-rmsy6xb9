class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isSeen = set()
        for num in nums:
            if num in isSeen:
                return True
            isSeen.add(num)
        return False