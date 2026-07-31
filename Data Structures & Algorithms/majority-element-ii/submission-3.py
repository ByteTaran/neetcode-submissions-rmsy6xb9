class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numsFreq = defaultdict(int)

        for num in nums:
            numsFreq[num] += 1

            if len(numsFreq) < 3:
                continue
            
            newCount = defaultdict(int)
            for num, count in numsFreq.items():
                if count > 1:
                    newCount[num] = count - 1
                
            numsFreq = newCount
        res = list()
        for key in numsFreq.keys():
            if nums.count(key) > len(nums) // 3:
                res.append(key)

        return res
