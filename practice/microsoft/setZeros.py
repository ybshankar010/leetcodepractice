class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows,zero_cols = set(), set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for row in zero_rows:
            matrix[row] = [0] * len(matrix[0])
        

        for col in zero_cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
    
        return

if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution = Solution()
    solution.setZeroes(matrix)
    print(matrix)