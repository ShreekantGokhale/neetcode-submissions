class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, len(prices)-1
        p = 0
        while l<len(prices)-1:
            while r>l:
                d = prices[r]-prices[l]
                p = max(p, d)
                r-=1
            l += 1
            r = len(prices)-1

        return p


        