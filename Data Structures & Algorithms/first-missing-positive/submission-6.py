class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        minPosNum = 1

        for num in nums:
            if num > 0:
                if minPosNum == num:
                    minPosNum += 1
                elif minPosNum < num:
                    return minPosNum
            
        
        return minPosNum