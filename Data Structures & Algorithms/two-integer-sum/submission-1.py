class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        s = set()
        for i in range(len(nums)):
            s.add(nums[i])
            d[i] = target-nums[i]
            if d[i] in s:
                if nums.index(d[i]) != i:
                    return [nums.index(d[i]), i]
        return False
        