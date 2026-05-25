class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l,r = 0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                p = prices[r]-prices[l]
                mp = max(mp,p)
            else:
                l = r
            r += 1

        return mp