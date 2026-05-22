class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums: return 0
        
        nums.sort()
        v = 0
        ptr = 0
        
        while ptr < len(nums):
            # Start streak at 1 because a single number is a sequence of 1
            cur = 1 
            
            while ptr + 1 < len(nums):
                # Case 1: Consecutive numbers
                if nums[ptr] == nums[ptr+1] - 1:
                    cur += 1
                    ptr += 1
                # Case 2: Duplicate numbers (ignore them, don't break the streak)
                elif nums[ptr] == nums[ptr+1]:
                    ptr += 1
                # Case 3: Gap found
                else:
                    break
            
            v = max(v, cur)
            ptr += 1
            
        return v