class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freq = self.freq_fun(nums)
    #     sorted_freq = sorted([(k,v) for k,v in freq.items()], key=lambda z: -z[1])
    #     return [x[0] for x in sorted_freq[:k]]
    # def freq_fun(self, nums):
    #     a = {}
    #     for i in nums:
    #         a[i] = a.get(i,0) + 1
    #     return a
        c_d = {}	
        for i in nums:
            c_d[i] = c_d.get(i,0)+1
        
        frequency = sorted([(no,val)  for no,val in c_d.items()], key=lambda x: x[1], reverse=True)
        return [no for no,val in frequency[:k]]