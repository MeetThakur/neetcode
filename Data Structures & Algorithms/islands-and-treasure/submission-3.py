from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])

        q = deque()
        visited = set()

        def ac(i,j):
            if i<0 or i>rows-1:
                return 
            if j<0 or j>cols -1:
                return 
            
            if (i,j) in visited or grid[i][j] == -1:
                return

            q.append([i,j])
            visited.add((i,j))

            return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))
            
        curr = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = curr
                ac(r+1,c)
                ac(r-1,c)
                ac(r,c+1)
                ac(r,c-1)

            curr += 1




