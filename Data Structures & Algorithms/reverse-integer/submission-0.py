class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        n = abs(x)
        while n!=0:
            r = n%10
            rev = rev*10+r
            if rev>(2**31-1):
                return 0
            n = n//10
        return rev if x>0 else -rev