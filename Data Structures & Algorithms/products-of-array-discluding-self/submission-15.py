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
        res = list()
        for num in nums:
            if 0 in nums and num != 0:
                res.append(0)
            elif num == 0:
                res.append(product)
            else:
                res.append(product // num)
        
        return res