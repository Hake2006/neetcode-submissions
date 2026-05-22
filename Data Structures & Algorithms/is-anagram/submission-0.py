from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = Counter(s)
        hash2 = Counter(t)
        if hash1 == hash2:
            return True
        else:
            return False