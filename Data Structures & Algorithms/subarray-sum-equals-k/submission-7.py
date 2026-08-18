class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sumTrack = {0:1}
        sumNum = 0
        for num in nums:
            sumNum += num
            ans += sumTrack.get(sumNum - k, 0)
            sumTrack[sumNum] = sumTrack.get(sumNum, 0) + 1
        
        return ans