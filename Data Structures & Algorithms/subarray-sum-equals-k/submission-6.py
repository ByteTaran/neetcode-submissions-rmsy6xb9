class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        trackSum = {0:1}
        sumArr = 0
        for num in nums:
            sumArr += num
            ans += trackSum.get(sumArr - k, 0)
            trackSum[sumArr] = trackSum.get(sumArr, 0) + 1
        return ans