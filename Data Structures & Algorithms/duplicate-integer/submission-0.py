from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = Counter(nums)
        for i in hash.values():
            if i>1:
                return True
        return False