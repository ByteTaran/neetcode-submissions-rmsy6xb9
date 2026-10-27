class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = left = rightMax = waterTrapped = 0
        right = len(height) - 1
        while left <= right:
            if height[left] <= height[right]:
                if leftMax - height[left] <= 0:
                    waterTrapped += 0
                else:
                    waterTrapped += leftMax - height[left]
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                if rightMax - height[right] <= 0:
                    waterTrapped += 0
                else:
                    waterTrapped += rightMax - height[right]

                rightMax = max(rightMax, height[right])
                right -= 1
        
        return waterTrapped