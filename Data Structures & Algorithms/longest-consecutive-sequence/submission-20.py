class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longestSequence = 1
        nums = set(nums)
        for num in nums:
            if not num - 1  in nums:
                sequence = 0
                number = num
                while number in nums:
                    number += 1
                    sequence += 1
                longestSequence = max(longestSequence, sequence)


        return longestSequence