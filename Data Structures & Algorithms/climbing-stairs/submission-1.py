class Solution:
    def climbStairs(self, n: int) -> int:
        # if n<=2:
        #     return n
        # else:
        #     return self.climbStairs(n-1)+self.climbStairs(n-2)

        if n==1:
            return 1
        elif n==2:
            return 2
        ls2 = [1,2]
        for i in range(3,n):
            ls2 = [ls2[-1],sum(ls2)]
        return sum(ls2)