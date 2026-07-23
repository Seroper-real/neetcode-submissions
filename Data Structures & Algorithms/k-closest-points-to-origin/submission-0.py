class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for point in points:
            dist = math.sqrt(math.pow(point[0],2) + math.pow(point[1],2))
            dists.append(self.DistPoint(point, dist))

        heapq.heapify(dists)
        result = []

        for _ in range(k):
            result.append(heapq.heappop(dists).point)

        return result

    class DistPoint:
        def __init__(self, point: List[int], dist: float) -> None:
            self.point = point
            self.dist = dist

        def __lt__(self, other: DistPoint) -> bool:
            return self.dist < other.dist