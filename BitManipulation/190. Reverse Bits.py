class Solution:
    def reverseBits(self, n: int) -> int:

        # remainder_lst = [0]*32
        # quotient, remainder = divmod(n, 2)
        # remainder_lst[-1] = remainder
        # index_i = -1
        # while quotient > 0:
        #     index_i = index_i-1
        #     print(quotient, remainder)
        #     quotient, remainder = divmod(quotient, 2)
        #     remainder_lst[index_i] = remainder
        
        # out = 0
        # for idx, i in enumerate(remainder_lst):
        #     out = out + i*2**idx
        # return out
        
        quotient, remainder = divmod(n, 2)
        idx = 31
        out = remainder*2**idx
        while quotient > 0:
            idx = idx -1
            quotient, remainder = divmod(quotient, 2)
            out = out + remainder*2**idx
        
        return out


        # Convert integer to bit: 
        # Continuesly divide integer by 2 and get remainder and reverse order of remainder will be binary 
        # Convert binary to integer:
        # Sum the values * 2 power of index from right of binary
        # The time complexity is O(1) because the input is bounded by a fixed 32-bit integer size, meaning the algorithm performs at most 32 operations.
        # Space Complexity:O(1)


