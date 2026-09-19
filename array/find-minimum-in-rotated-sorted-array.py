class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]
        for i in range(len(nums)):
            if nums[i]<res:
                res=nums[i]
            
        return res