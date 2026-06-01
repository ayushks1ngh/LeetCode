class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        result = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)

        return [list(x) for x in result]