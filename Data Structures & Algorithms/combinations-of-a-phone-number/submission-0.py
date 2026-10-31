class Solution:
    def letterCombinations(self, digits):
        res = []
        if len(digits)==0:
            return res
        n = len(digits)
        d = {2: list("abc"), 3: list("def"), 4: list("ghi"), 5: list("jkl"), 6: list("mno"),
             7: list("pqrs"), 8: list("tuv"), 9: list("wxyz")}
        i = 0
        ls1 = []
        ls2 = d[int(digits[0])]
        i +=1
        res.extend(self.two_list_comb(ls1, ls2))
        while (i < len(digits)):
            ls1 = res
            ls2 = d[int(digits[i])]
            res = self.two_list_comb(ls1, ls2)
            i += 1
        return res

    def two_list_comb(self, ls1, ls2):
        ls = []
        if not ls1:
            return list(ls2)
        for i in ls1:
            for j in ls2:
                ls.append(i + j)
        return ls