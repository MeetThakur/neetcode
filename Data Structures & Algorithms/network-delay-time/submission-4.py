class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int):
        g = {}
        for i in range(1, n + 1):
            g[i] = []
        for u, v, t in times:
            g[u].append((v, t))

        mh = [(0,k)]
        vis = set()
        t = 0
        while mh:
            x,nx = heapq.heappop(mh)
            if nx in vis:
                continue
            vis.add(nx)

            t = x
            for i in g[nx]:
                heapq.heappush(mh,(i[1]+x,i[0]))


        if len(vis) == n:
            return t
        
        return -1

