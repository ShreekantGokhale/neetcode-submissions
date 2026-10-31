# class Solution:
#     def groupAnagrams(self, strs):
#         d = {}
#         for i in range(len(strs)):
#             k = ''.join(sorted(strs[i])) 
#             if k in d:
#                 d[k].append(i)
#             else:
#                 d[k] = [i]
            
#         a = []
#         t = 0
#         for i,j in d.items():
#             a.append([])
#             for x in j:
#                 a[t].append(strs[x])
#             t += 1
        
#         return a
    

    # def hs(self, s):
    #     r = {}
    #     for i in s:
    #         r[i] = 1 + r.get(i,0)
    #     return r

class Solution:
  def groupAnagrams(self, strs: list[str]):
    types = set()
    type_dict = {}
    for i in strs:
      a = self.create_hash(i)
      if a in types:
        type_dict[a].append(i)
      else:
        types.add(a)
        type_dict[a] = [i]
    return [type_dict[x] for x in type_dict.keys()]
          
  def create_hash(self, s: str):
    r = {}
    for i in s:
      r[i] = r.get(i,0) + 1
    return frozenset(r.items())