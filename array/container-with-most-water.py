class Solution:
    def maxArea(self, height: List[int]) -> int:

        ans = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                ans = max(ans, area)

        return ans