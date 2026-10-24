class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        countSubArray = 0
        sumOccurance = {0:1}
        sumArray = 0
        
        for num in nums:
            sumArray += num
            countSubArray += sumOccurance.get(sumArray - k, 0)
            sumOccurance[sumArray] = sumOccurance.get(sumArray, 0) + 1

        return countSubArray