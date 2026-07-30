class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 0
        for num in nums:
            sequence = 1
            if not num - 1 in nums:
                nextNum = num
                while nextNum + 1 in nums:
                    nextNum += 1
                    sequence += 1
                longest = max(longest, sequence)
        
        return longest
