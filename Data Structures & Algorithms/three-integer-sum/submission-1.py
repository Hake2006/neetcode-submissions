class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i + 1, n - 1
            while j < k: # Use < because we need 3 distinct indices
                s = nums[i] + nums[j] + nums[k]
                
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    # Crucial: Move pointers and skip duplicates for j and k
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                        
        return res