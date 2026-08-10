class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = set()
        for i in range(len(nums)):
            countFreq = 0
            if nums[i] not in ans:
                for j in range(len(nums)):
                    if nums[i] == nums[j]:
                        countFreq += 1
                
                    if countFreq > len(nums) // 3:
                        ans.add(nums[i])
                        break
        return list(ans)