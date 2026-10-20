class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        countZero = 0
        res = list()
        for num in nums:
            if num == 0:
                countZero += 1
            else:
                product *= num
        
        if countZero > 1:
            return [0] * len(nums)
        
        for num in nums:
            if num == 0:
                res.append(product)
            elif countZero:
                res.append(0)
            else:
                res.append(product // num)
        return res