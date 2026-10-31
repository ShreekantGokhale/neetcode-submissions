class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        t_d = dict()
        for i in range(len(numbers)):
            if numbers[i] not in t_d:
                t_d[target - numbers[i]] = i
            else:
                return [t_d[numbers[i]]+1,i+1]
        return []