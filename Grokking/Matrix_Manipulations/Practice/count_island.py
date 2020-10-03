
class Solution:
    def __init__(self, grid):
        self.row = len(grid)
        self.col = len(grid[0])
        self.grid = grid
        self.visited = [[False for _ in range(self.col)] for _ in range(self.row)]

    def dfs(self, i, j):
        if (not i in range(self.row)) or (not j in range(self.col)) or (self.visited[i][j]) or (not self.grid[i][j]):
            return
        self.visited[i][j] = True
        self.dfs(i-1, j)
        self.dfs(i+1, j)
        self.dfs(i, j-1)
        self.dfs(i, j+1)

    def count_islands(self):
        if not self.grid:
            return 0

        global_count = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] and (not self.visited[i][j]):
                    self.dfs(i, j)
                    global_count += 1
        return global_count

def main():
    grid = [ [1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0] ]
    print (Solution(grid).count_islands()) #1

    grid = [ [1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1] ]
    print (Solution(grid).count_islands()) #3

main()
