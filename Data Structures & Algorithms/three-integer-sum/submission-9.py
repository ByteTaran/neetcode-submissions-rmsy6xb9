class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1
                
                while left < right:
                    triplets = [nums[i], nums[left], nums[right]]
                    if sum(triplets) < 0:
                        left += 1
                    elif sum(triplets) > 0:
                        right -= 1
                    else:
                        res.append(triplets)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
        return list(triplet for triplet in res)
                        