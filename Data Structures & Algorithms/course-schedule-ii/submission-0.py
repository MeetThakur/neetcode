class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        g = {}
        id = [0] * n

        for i in range(n):
            g[i] = []

        for a, b in pre:
            g[b].append(a) 
            id[a] += 1  
        q = deque()

        for i in range(n):
            if id[i] == 0:
                q.append(i)

        ans = []

        while q:
            node = q.popleft()
            ans.append(node)

            for i in g[node]:
                id[i] -= 1
                if id[i] == 0:
                    q.append(i)

        if len(ans) != n:
            return []

        return ans