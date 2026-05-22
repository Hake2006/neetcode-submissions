from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Count frequencies
        counts = Counter(nums) 
        
        # 2. Sort by value (frequency) in descending order
        # We use [1] because items() returns (key, value)
        sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        
        # 3. Extract the first k keys
        return [item[0] for item in sorted_items[:k]]