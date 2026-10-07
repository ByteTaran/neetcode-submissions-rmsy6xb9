class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numfreq = dict()

        for num in nums:
            numfreq[num] = numfreq.get(num, 0) + 1

            if len(numfreq) == 3:
                temp = dict()
                for num, freq in numfreq.items():
                    if numfreq[num] > 1:
                        temp[num] = freq - 1
                numfreq = temp
        res = list()
        for num, freq in numfreq.items():
            if freq > (len(nums) // 3):
                res.append(num)
                continue
            if nums.count(num) > (len(nums) // 3):
                res.append(num)
        
        return res
                    