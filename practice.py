class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int):
        from collections import defaultdict
        import heapq

        graph = defaultdict(list)
        for a, b, p in flights:
            graph[a].append((b, p))

        Q = [(0, src, k)]
        visited = dict()

        while Q:
            p1, a, t = heapq.heappop(Q)
            if a == dst:
                return p1
            if t >= 0 and (a not in visited or visited[a] < t):
                for b, p2 in graph[a]:
                    heapq.heappush(Q, (p1 + p2, b, t - 1))
                visited[a] = t

        return -1


print(
    Solution().findCheapestPrice(
        5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2
    )
)

