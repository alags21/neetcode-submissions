class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1

        total = 0
        left_max = height[L]
        right_max = height[R]

        while L < R:
            if height[L] <= height[R]:
                left_max = max(height[L], left_max)
                total += left_max - height[L]
                L += 1
            else:
                right_max = max(height[R], right_max)
                total += right_max - height[R]
                R -=1
        
        return total

