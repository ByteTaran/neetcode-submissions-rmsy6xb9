class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        ans = 0
        trackSum = {0:1}
        for num in nums:
            preSum += num
            ans += trackSum.get(preSum - k, 0)
            trackSum[preSum] = trackSum.get(preSum, 0) + 1
            
        return ans