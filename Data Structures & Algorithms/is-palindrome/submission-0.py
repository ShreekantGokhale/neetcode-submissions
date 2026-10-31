class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_fin = ''
        for i in s:
            if i.isalnum():
                s_fin += i.lower()
            else:
                continue
         
        l,r = 0, len(s_fin)-1
        while l<=r:
            if s_fin[l] == s_fin[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True