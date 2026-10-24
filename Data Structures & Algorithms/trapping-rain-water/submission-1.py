class Solution:
    def trap(self, height: List[int]) -> int:
        left = leftMax = rightMax = waterTrapped = 0
        right = len(height) - 1

        while left <= right:
            if height[left] <= height[right]:
                waterTrapped += max(0, leftMax - height[left])
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                waterTrapped += max(0, rightMax - height[right])
                rightMax = max(rightMax, height[right])
                right -= 1

        return waterTrapped