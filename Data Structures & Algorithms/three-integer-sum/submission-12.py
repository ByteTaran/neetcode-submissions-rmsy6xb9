class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = list()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                triplet = [nums[i],nums[left],nums[right]]
                if sum(triplet) < 0:
                    left += 1
                elif sum(triplet) > 0:
                    right -= 1
                else:
                    triplets.append(triplet) 
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return triplets