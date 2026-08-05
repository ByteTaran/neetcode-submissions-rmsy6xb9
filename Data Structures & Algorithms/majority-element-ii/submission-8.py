class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        checkFreq = dict()
        res = list()
        for num in nums:
                checkFreq[num] = checkFreq.get(num, 0) + 1
                if num not in res and checkFreq[num] > len(nums) // 3:
                    res.append(num)
                if len(checkFreq) == 3:
                    tempFreq = dict()
                    for key, val in checkFreq.items():
                        if val > 1:
                            tempFreq[key] = val - 1
                    
                    checkFreq = tempFreq

        for key in checkFreq:
            countFreq = 0
            if key not in res:
                for num in nums:
                    if num == key:
                        countFreq += 1
                        if countFreq > len(nums) // 3:
                            res.append(num)
                            break
        return res