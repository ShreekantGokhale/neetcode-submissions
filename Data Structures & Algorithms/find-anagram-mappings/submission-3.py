class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls = []
        for i,j in enumerate(nums1):
            k = nums2.index(j)
            while k in ls:
                k = nums2[k+1:].index(j)+k+1
            ls.append(k)
        return ls
        
