class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mb = prices[0]
        mp = 0
        for sell in prices:
            mp = max(mp,sell-mb)
            mb = min(sell,mb)
        return(mp)