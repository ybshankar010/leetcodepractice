class Solution(object):
    def performTranspose(self,matrix):
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(i+1,cols):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        return

    def performReverse(self,matrix):
        rows, cols = len(matrix), len(matrix[0])

        for j in range(cols//2):
                swapped_col = cols-j-1
                for i in range(rows):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[i][swapped_col]
                    matrix[i][swapped_col] = temp
        return

    def rotate(self, matrix):
        self.performTranspose(matrix)
        self.performReverse(matrix)

if __name__ == "__main__":
    solution = Solution()
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    matrix = [[1]]
    solution.rotate(matrix)
    print(matrix)