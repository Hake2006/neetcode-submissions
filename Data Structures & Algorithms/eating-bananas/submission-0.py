import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc(list, k):
            v = 0
            for i in list:
                v += (i + k - 1) // k
            return v
            
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            m = (l + r) // 2
            v = calc(piles, m)
            if v <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res