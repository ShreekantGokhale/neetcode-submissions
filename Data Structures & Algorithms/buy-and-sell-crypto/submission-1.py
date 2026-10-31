class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        p = 0
        while l<len(prices)-1:
            while r<len(prices):
                d = prices[r]-prices[l]
                p = max(p, d)
                r+=1
            l += 1
            r = l+1

        return p


        