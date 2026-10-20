class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProduct = [1] * len(nums)
        suffProduct= [1] * len(nums)
        res = [1] * len(nums)

        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            preProduct[i] = product
        
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            suffProduct[i] = product
        
        for i in range(len(nums)):
            res[i] = preProduct[i] * suffProduct[i]
        

        return res


