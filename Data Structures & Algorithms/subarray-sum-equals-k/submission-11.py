class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        trackSum = {0:1}
        sumNum = 0
        countArray = 0

        for num in nums:
            sumNum += num
            countArray += trackSum.get(sumNum - k, 0)
            trackSum[sumNum] = trackSum.get(sumNum, 0) + 1
        return countArray
