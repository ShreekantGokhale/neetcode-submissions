class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for i in range(len(strs)):
            k = ''.join(sorted(strs[i])) 
            if k in d:
                d[k].append(i)
            else:
                d[k] = [i]
            
        a = []
        t = 0
        for i,j in d.items():
            a.append([])
            for x in j:
                a[t].append(strs[x])
            t += 1
        
        return a
    

    # def hs(self, s):
    #     r = {}
    #     for i in s:
    #         r[i] = 1 + r.get(i,0)
    #     return r

