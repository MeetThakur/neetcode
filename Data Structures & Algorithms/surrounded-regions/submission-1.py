from typing import List

class Solution:
    def solve(self, b: List[List[str]]) -> None:
        if not b:
            return

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return

            if b[i][j] == 'X' or b[i][j] == '#':
                return

            b[i][j] = '#'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        row = len(b)
        col = len(b[0])

        for i in range(row):
            for j in range(col):
                if (i == 0 or i == row - 1 or j == 0 or j == col - 1) and b[i][j] == 'O':
                    dfs(i, j)

        for i in range(row):
            for j in range(col):
                if b[i][j] == 'O':
                    b[i][j] = 'X'
                elif b[i][j] == '#':
                    b[i][j] = 'O'