class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        countArray = 0
        sumArray = 0
        trackDiff = {0:1}

        for num in nums:
            sumArray += num
            countArray += trackDiff.get(sumArray - k, 0) 
            trackDiff[sumArray] = trackDiff.get(sumArray, 0) + 1
        
        return countArray