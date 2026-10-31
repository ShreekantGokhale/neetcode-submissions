class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=2:
            return min(cost)
        # cost2 = [cost[0],min(cost[:2])]
        cost2 = [0,0]
        n = len(cost)
        for i in range(2,n):
            res = min([(cost2[0]+cost[i-2]),(cost2[1]+cost[i-1])])
            cost2 = [cost2[-1],res]
        return min([(cost2[0]+cost[n-2]),(cost2[1]+cost[n-1])])