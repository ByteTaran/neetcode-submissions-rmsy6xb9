class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minLR = [0] * len(height)
        waterTrapped = [0] * len(height)

        maxHeight = 0
        for i in range(1,len(height)):
            maxHeight = max(maxHeight, height[i - 1])
            maxLeft[i] = maxHeight
        
        maxHeight = 0
        for i in range(len(height) - 2, -1, -1):
            maxHeight = max(maxHeight, height[i + 1])
            maxRight[i] = maxHeight

        for i in range(len(height)):
            minLR[i] = min(maxLeft[i],maxRight[i])
        
        for i in range(len(height)):
            if minLR[i] - height[i] < 0:
                waterTrapped[i] = 0
            else:
                waterTrapped[i] = minLR[i] - height[i]

        return sum(waterTrapped)