class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]] 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                nexR, nexC = r + dr, c + dc
                if (nexR < 0 or nexC < 0 or
                    nexR == N or nexC == N or
                    (nexR, nexC) in visit
                ):
                    continue
                visit.add((nexR, nexC))
                heapq.heappush(minH, [max(t, grid[nexR][nexC]), nexR, nexC])