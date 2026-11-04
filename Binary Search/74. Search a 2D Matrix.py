class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:


        button, top = 0,len(matrix)-1

        while button <= top:
            mid = button + (top-button)//2

            if target < matrix[mid][0]:
                top = mid-1
            elif target > matrix[mid][-1]:
                button = mid + 1
            else:
                break
        if button > top:
            return False
        
        row = button + (top-button)//2

        l,r = 0, len(matrix[row])-1

        while l <= r:
            mid = l + (r-l)//2

            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid -1
            else:
                l = mid + 1
        
        return False

        # Time complexity: O(logm + logn)
        # Space complexity O(1)
        # 这一题很快的就想到了binary search row ， col， 但最大的问题是所有边界都没想清楚
        # 1. row 和col 的最大边界是len（）-1， 算 mid index 还是要len -1 de
        # 第二个是exist 的边界没想清楚，没仔细讨论while loop exist 的可能性就开始写了
        




