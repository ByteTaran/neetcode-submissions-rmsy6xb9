class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        res = [0] * numsLen
        preProducts = [0] * numsLen
        postProducts = [0] * numsLen

        preProducts[0] = 1
        postProducts[-1] = 1
        preProduct = postProduct = 1
        for i in range(1, numsLen):
            preProduct *= nums[i - 1] 
            preProducts[i] = preProduct
        for i in range(numsLen - 2, -1, -1):
            postProduct *= nums[i + 1]
            postProducts[i] = postProduct
        for i in range(numsLen):
            res[i] = preProducts[i] * postProducts[i]

        return res