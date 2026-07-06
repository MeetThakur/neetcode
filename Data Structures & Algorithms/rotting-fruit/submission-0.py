from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        def amr(i, j):
            if not (0 <= i < rows and 0 <= j < cols):
                return

            if grid[i][j] == 1:
                grid[i][j] = 2
                q.append((i, j))

        # Add all initially rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))

        minutes = 0

        while q:
            size = len(q)
            changed = False

            for _ in range(size):
                row, col = q.popleft()

                old = len(q)
                amr(row + 1, col)
                amr(row - 1, col)
                amr(row, col + 1)
                amr(row, col - 1)

                if len(q) > old:
                    changed = True

            if changed:
                minutes += 1

        for row in grid:
            if 1 in row:
                return -1

        return minutes