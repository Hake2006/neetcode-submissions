class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x,y in points:
            dt = x**2 + y**2
            heapq.heappush(h,[-dt,[x,y]])
            if len(h)>k:
                heapq.heappop(h)
        return [p[1] for p in h]