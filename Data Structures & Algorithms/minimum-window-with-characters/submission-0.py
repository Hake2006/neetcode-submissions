class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        ct = Counter(t)
        w = {}
        h,n = 0,len(ct)
        res,ans = [-1,-1],float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            w[c] = 1 + w.get(c,0)
            if c in ct and w[c]==ct[c]:
                h += 1
            while h == n:
                if (r-l+1)<ans:
                    res = [l,r]
                    ans = r-l+1
                w[s[l]] -= 1
                if s[l] in ct and w[s[l]]<ct[s[l]]:
                    h -= 1
                l += 1
        l,r = res
        return s[l:r+1] if ans != float('inf') else ""