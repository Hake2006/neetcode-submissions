from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        n = len(height)
        lm = [0] * n
        rm = [0] * n
        
        # 1. Build the Left Max array
        lm[0] = height[0]
        for i in range(1, n):
            lm[i] = max(lm[i-1], height[i])
            
        # 2. Build the Right Max array
        rm[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rm[i] = max(rm[i+1], height[i])
            
        # 3. Calculate trapped water
        ans = 0
        for i in range(n):
            # The water trapped above block i is the minimum of its 
            # left and right tallest boundaries, minus its own height.
            ans += min(lm[i], rm[i]) - height[i]
            
        return ans