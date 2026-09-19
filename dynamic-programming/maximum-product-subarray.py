class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [(float('-inf'), float('inf'))] * n
        dp[0] = (nums[0], nums[0])

        ans = nums[0]

        for i in range(1, n):
            prev_max, prev_min = dp[i - 1]
            num = nums[i]

            if num < 0:
                curr_max = max(prev_min * num, num)
                curr_min = min(prev_max * num, num)
            else:
                curr_max = max(prev_max * num, num)
                curr_min = min(prev_min * num, num)

            dp[i] = (curr_max, curr_min)
            ans = max(ans, curr_max)

        return ans