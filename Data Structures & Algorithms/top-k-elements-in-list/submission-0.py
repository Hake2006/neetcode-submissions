from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = Counter(nums)        
        sh = dict(sorted(hash.items(), key=lambda item: item[1]))
        return list(list(sh.keys())[-k:])