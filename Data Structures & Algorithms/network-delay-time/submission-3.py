class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int):
        g = {}

        for i in range(1, n + 1):
            g[i] = []

        for u, v, t in times:
            g[u].append([v, t])

        res = {node: float("inf") for node in range(1, n + 1)}

        def dfs(i, t):
            if t >= res[i]:          
                return

            res[i] = t

            for v, w in g[i]:
                dfs(v, t + w)

        dfs(k, 0)

        ans = max(res.values())

        return ans if ans != float("inf") else -1