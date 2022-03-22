class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        from collections import defaultdict

        global ans

        graph = defaultdict(list)
        for a, b, p in sorted(flights, key=lambda x: (x[2])):
            graph[a].append((b, p))

        ans = 100000

        def dfs(a, p=0, t=-1):
            global ans
            if t > k or p > ans:
                return False
            if a == dst:
                ans = min(ans, p)
                return True
            for b, p2 in graph[a]:
                if not dfs(b, p + p2, t + 1):
                    break
            return True

        visited = set()

        def available(a, t=-1):
            if a in visited or t > k:
                return
            else:
                visited.add(a)
            if a == dst:
                visited.add(a)
                return
            for b, p in graph[a]:
                available(b, t + 1)

        available(src)
        if dst in visited:
            dfs(src)
            return ans
        else:
            return -1


arr4 = [4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1]

print(Solution().findCheapestPrice(*arr4))

