class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1] * len(nums)
        suffixProduct = [1] * len(nums)
        products = [1] * len(nums)

        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            prefixProduct[i] = product
        
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            suffixProduct[i] = product
            
        for i in range(len(nums)):
            products[i] = prefixProduct[i] * suffixProduct[i]
        
        return products