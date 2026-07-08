class Solution:
    def canFinish(self, nc: int, pre: List[List[int]]) -> bool:
        g = {}
        for a, b in pre:
            if a not in g:
                g[a] = []

            g[a].append(b)

        def dfs(node, path):
            if node in path:
                return False

            if node not in g:
                return True

            path.add(node)

            for i in g[node]:
                if not dfs(i, path):
                    return False

            path.remove(node)
            g[node] = []

            return True

        for i in g:
            if not dfs(i, set()):
                return False

        return True