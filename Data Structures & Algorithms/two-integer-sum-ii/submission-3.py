class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # t_d = dict()
        # for i in range(len(numbers)):
        #     if numbers[i] not in t_d:
        #         t_d[target - numbers[i]] = i
        #     else:
        #         return [t_d[numbers[i]]+1,i+1]
        # return []
        #This is o(n) in space
        # Hence two pointer
        l = 0
        r = len(numbers)-1
        while l<r:
            cursum = numbers[l]+numbers[r]
            if cursum<target:
                l += 1
            elif cursum>target:
                r -= 1
            else:
                return [l+1,r+1]
