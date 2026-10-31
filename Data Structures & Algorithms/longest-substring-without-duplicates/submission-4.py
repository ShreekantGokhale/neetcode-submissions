class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        t_d = set()
        l = 0
        max_len = 1
        for r in range(len(s)):
            while s[r] in t_d:
                max_len = max(max_len, len(t_d))
                t_d.remove(s[l])
                l += 1
            t_d.add(s[r])
        return max(max_len,len(t_d))