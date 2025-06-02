class Solution(object):

    ROW_TRAVERSAL = [-1,1,0,0]
    COL_TRAVERSAL = [0,0,-1,1]

    def dfs(self,grid,row,col):
        rows = len(grid)
        cols = len(grid[0])
        grid[row][col] = "-1"

        for move_row,move_col in zip(self.ROW_TRAVERSAL,self.COL_TRAVERSAL):
            next_row = row + move_row
            next_col = col + move_col

            if next_row >=0 and next_row<rows and next_col>=0 and next_col < cols and grid[next_row][next_col] == "1":
                self.dfs(grid,next_row,next_col)

        return

    def numIslands(self, grid):

        rows = len(grid)
        cols = len(grid[0])
        print(rows,"<>",cols)
        num_islads = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    num_islads += 1
                    self.dfs(grid,i,j)
        
        return num_islads


if __name__ == "__main__":
    matrix = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    solution = Solution()
    print(solution.numIslands(matrix))