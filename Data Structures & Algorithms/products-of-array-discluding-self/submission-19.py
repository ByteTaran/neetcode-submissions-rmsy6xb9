class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       preProduct = [1] * len(nums)
       sufProduct = [1] * len(nums)
        
       product = 1
       for i in range(1, len(preProduct)):
            product *= nums[i - 1]
            preProduct[i] = product
        
       product = 1
       for i in range(len(preProduct) - 2, -1, -1):
            product *= nums[i + 1]
            sufProduct[i] = product
        
       productNums = list()
       for i in range(len(nums)):
            productNums.append(preProduct[i] * sufProduct[i])
        
       return productNums