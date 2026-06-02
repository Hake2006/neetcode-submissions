class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = Counter(nums)
        for num,freq in d.items():
            if d[num] > 1:
                return num