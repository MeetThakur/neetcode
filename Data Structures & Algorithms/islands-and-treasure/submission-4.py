from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])

        def find(i, j):
            q = deque([(i, j, 0)])
            visited = {(i, j)}

            while q:
                r, c, d = q.popleft()

                if grid[r][c] == 0:
                    return d

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] != -1 and
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc, d + 1))

            return 2147483647

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2147483647:
                    grid[i][j] = find(i, j)



                    