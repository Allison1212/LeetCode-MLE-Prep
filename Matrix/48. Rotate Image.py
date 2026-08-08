class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        r = len(matrix) - 1
        n = len(matrix) - 1
        x = y = 0

        while x < r:
            while y < r:
                int_val = matrix[x][y]
                matrix[x][y] = matrix[n-y][x]
                matrix[n-y][x] = matrix[r][n-y]
                matrix[r][n-y] = matrix[y][r]
                matrix[y][r] = int_val
                y+=1
            r-=1

            x +=1
            y = x