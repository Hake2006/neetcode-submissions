class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c,0)

        n = len(s1)
        l,r = 0,n
        
        count2 = {}
        wdw = s2[l:r]
        for c in wdw:
            count2[c] = 1 + count2.get(c,0)

        while r < len(s2):
            if count1 == count2:
                return True
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            l += 1
            r += 1
        return count1 == count2