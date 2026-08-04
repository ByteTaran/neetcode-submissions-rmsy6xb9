class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        countSubArrays = 0
        trackPrefixSum = {0:1}
        for num in nums:
            prefixSum += num
            countSubArrays += trackPrefixSum.get(prefixSum - k, 0)
            trackPrefixSum[prefixSum] = trackPrefixSum.get(prefixSum, 0) + 1
        return countSubArrays