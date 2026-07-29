class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = list()
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            res.append(product)
        
        return res