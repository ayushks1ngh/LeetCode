class Solution:
    def maxProfit(self, nums):
        mn = 30001
        sm = 0
        for num in nums:
            if num > mn:
                sm += num - mn
            mn = num
        return sm