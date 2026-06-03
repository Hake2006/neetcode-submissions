class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms,cs = nums[0],0
        for num in nums:
            if cs<0:
                cs = 0
            cs += num
            ms = max(ms,cs)
        return ms