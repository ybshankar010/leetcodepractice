class Solution(object):
    def spiralOrder(self, matrix):
        left, right = (0,1),(0,-1)
        up, down = (-1,0),(1,0)
        spiralOrder = []
        rows, cols = len(matrix),len(matrix[0])
        totalCount = rows * cols

        direction = left
        prev = (0,-1)

        while len(spiralOrder) != totalCount:
            for _ in range(cols) :
                next = (prev[0]+direction[0],prev[1]+direction[1])
                # print(prev,"<>", next,"<>",spiralOrder)
                spiralOrder.append(matrix[next[0]][next[1]])
                prev = next
            
            rows -= 1

            if direction == left:
                direction = down
            elif direction == right:
                direction = up
            
            for _ in range(rows):
                next = (prev[0]+direction[0],prev[1]+direction[1])
                # print(prev,"<>", next,"<>",spiralOrder)
                spiralOrder.append(matrix[next[0]][next[1]])
                prev = next
            
            cols -= 1


            if direction == down:
                direction = right
            elif direction == up:
                direction = left
        
        return spiralOrder



if __name__ == "__main__":
    solution = Solution()
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1]]
    print(solution.spiralOrder(matrix))