class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i,0)
        
        for i in nums:
            prod.append(self.get_prod(d,i))
        
        return prod

    def get_prod(self, d, i):
        e = d.copy()
        e[i] -= 1
        res = 1
        for k in e.keys():
            res *= pow(k,e[k])
        return res
