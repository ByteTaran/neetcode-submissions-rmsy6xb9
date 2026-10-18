class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        triplet = list()

        def kSum(k, start, target) -> None:
            if k == 2:
                left = start
                right = len(nums) - 1

                while left < right:
                    if nums[left] + nums[right] < target:
                        left += 1
                    elif nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        res.append(triplet + [nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                return

            for i in range(start, len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                triplet.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                triplet.pop()


        kSum(3, 0, 0)
        return res