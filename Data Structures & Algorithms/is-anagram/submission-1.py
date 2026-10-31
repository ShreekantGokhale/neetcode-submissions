# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_dict = self.counter_dict(s)
#         t_dict = self.counter_dict(t)
#         return s_dict==t_dict


#     def counter_dict(self, s):
#         s_dict = {}
#         for i in s:
#             if i in s_dict:
#                 s_dict[i] += 1
#             else:
#                 s_dict[i] = 1    
#         return s_dict

class Solution:
  def isAnagram(self, s: str, t:str) -> bool:
    return self.make_hash(s) == self.make_hash(t)

  def make_hash(self,s) -> dict:
    result = {}
    for i in s:
      result[i] = result.get(i,0) + 1
    return result