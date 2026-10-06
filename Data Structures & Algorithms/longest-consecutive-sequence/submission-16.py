class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) == 0:
            return 0
        longestCount = 1

        for num in nums:
            if not num - 1 in nums:
                count = 1
                seq = num + 1
                while seq in nums:
                    count += 1
                    seq += 1
                
                longestCount = max(longestCount, count)

        
        return longestCount


