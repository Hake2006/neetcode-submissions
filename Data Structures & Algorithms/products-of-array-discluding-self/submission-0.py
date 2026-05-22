class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r = 1,1
        n = len(nums)
        ar = [1]*n
        for i in range(n):
            ar[i] *= l
            l *= nums[i]
        for i in range(-1,-n-1,-1):
            ar[i] *= r
            r *= nums[i]
        return ar