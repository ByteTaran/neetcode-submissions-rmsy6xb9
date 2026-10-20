class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequence = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                sequence = 0
                number = num
                while number in nums:
                    sequence += 1
                    number += 1
                longestSequence = max(longestSequence, sequence)
        
        return longestSequence