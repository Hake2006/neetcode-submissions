class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cs = set()
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in cs:
                cs.remove(s[l])
                l += 1
            cs.add(s[r])
            ans = max(ans,r-l+1)
        return ans