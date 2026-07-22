class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = 0
        res = ''
        large_jump = (numRows - 1) * 2
        if numRows == 1:
            return s
        while row < numRows:
            row_str = ''
            i = row
            small_jump = (numRows - (row + 1)) * 2
            while i < len(s):
                row_str = row_str + s[i]
                if row != 0 and row != (numRows-1):
                    if i+small_jump < len(s):
                        row_str = row_str + s[i+small_jump]
                i +=large_jump

            res += row_str
            row +=1
        return res
        

        #找周期