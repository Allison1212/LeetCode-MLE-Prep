class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # # My Solution
        # O(n*m) space
        # row_set = set()
        # col_set = set()
        # for x in range(len(matrix)):
        #     for y in range(len(matrix[0])):
        #         if matrix[x][y] == 0:
        #             row_set.add(x)
        #             col_set.add(y)
        #     if x in row_set:
        #          matrix[x] = [0]*len(matrix[0])
        
        # for x in range(len(matrix)):
        #     for y in range(len(matrix[0])):
        #         if y in col_set:
        #             matrix[x][y] = 0

        # Better solution 
        # 用第一排打标签，但要考虑第一排第一列自身原来是0 的情况
        # O(1) space 
        row = len(matrix)
        col = len(matrix[0])
        row_0_zero = any(matrix[0][y] == 0 for y in range(col))
        col_0_zero = any(matrix[x][0] ==0 for x in range(row))

        for x in range(1,row):
            for y in range(1,col):
                if matrix[x][y] == 0:
                    matrix[x][0] = 0
                    matrix[0][y] = 0
                    
            if matrix[x][0] == 0:
                 matrix[x] = [0]*col
        
        for y in range(col):
            if matrix[0][y] == 0:
                for x in range(row):
                    matrix[x][y] = 0
        if row_0_zero:
            matrix[0] = [0]*col
        if col_0_zero:
            for x in range(len(matrix)):
                    matrix[x][0] = 0

        


        