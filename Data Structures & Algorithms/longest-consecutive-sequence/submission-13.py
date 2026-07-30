class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longestSequence = 0
        sequence = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] - nums[i - 1] == 1:
                 sequence += 1
            else:
                longestSequence = max(longestSequence, sequence)
                sequence = 1
        
        return max(longestSequence, sequence)
                