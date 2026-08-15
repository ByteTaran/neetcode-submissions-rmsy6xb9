class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        isSeen = dict()
        for i in range(len(numbers)):
            if (target - numbers[i]) in isSeen:
                return [isSeen[target - numbers[i]], i + 1]
            isSeen[numbers[i]] = i + 1