class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        from collections import defaultdict

        if not prerequisites:
            return True

        prerequisites.sort()
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)

        ans = []

        def dfs(a, path=[]):
            while graph[a]:
                b = graph[a].pop(0)
                if b in path:
                    ans.append(False)
                else:
                    dfs(b, path + [b])

        dfs(min(graph), path=[min(graph)])

        return len(ans) == 0


Solution().canFinish(
    1, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
)

