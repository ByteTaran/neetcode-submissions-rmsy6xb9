class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        countZero = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                countZero += 1
        
        if countZero > 1:
            return [0] * len(nums)
        
        productNums = list()
        for num in nums:
            if countZero and num == 0:
                productNums.append(product)
            elif countZero and num != 0:
                productNums.append(0)
            else:
                productNums.append(product // num)
        return productNums
