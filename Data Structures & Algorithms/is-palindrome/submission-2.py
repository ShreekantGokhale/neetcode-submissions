class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_fin = ''
        # for i in s:
        #     if i.isalnum():
        #         s_fin += i.lower()
        #     else:
        #         continue
         
        # l,r = 0, len(s_fin)-1
        # while l<=r:
        #     if s_fin[l] == s_fin[r]:
        #         l += 1
        #         r -= 1
        #     else:
        #         return False
        
        # return True
        l = 0
        r = len(s)-1
        while l<r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
            elif s[l].lower()==s[r].lower():
                l += 1
                r -= 1
                continue
            else:
                return False
        return True
        