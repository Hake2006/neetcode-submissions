class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        srtd = dict(sorted(cnt.items(), key=lambda item: item[1]))
        last_k = dict(reversed(list(islice(reversed(srtd.items()), k))))
        return list(last_k)