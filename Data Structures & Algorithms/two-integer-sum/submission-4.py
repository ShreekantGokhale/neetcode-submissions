# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         s = set()
#         for i in range(len(nums)):
#             s.add(nums[i])
#             d[i] = target-nums[i]
#             if d[i] in s:
#                 if nums.index(d[i]) != i:
#                     return [nums.index(d[i]), i]
#         return False
    
    # class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     prevMap = {}  # val -> index

    #     for i, n in enumerate(nums):
    #         diff = target - n
    #         if diff in prevMap:
    #             return [prevMap[diff], i]
    #         prevMap[n] = i

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i,num in enumerate(nums):
            if target - num in d:
                return [d[target-num],i]
            d[num] = i
        return False