class Solution:
    def hammingWeight(self, n: int) -> int:
        quotient, remainder = divmod(n, 2)
        out = remainder

        while quotient > 0:
            quotient, remainder = divmod(quotient, 2)
            out = out + remainder
        
        return out
        

        #  The "Shift and Mask" Technique
        # Your loop inspects every single bit of the 32-bit integer one by one, from right to left
        # n >> i (Right Shift): This takes the integer n and shifts all of its bits to the right by i positions. This effectively moves the i-th bit all the way to the very end (the least significant bit position)
        # & 1 (Bitwise AND): By performing a bitwise AND with 1 (000...0001), you wipe out all the higher bits and isolate just that single rightmost bit.If the bit was a 1, (n >> i) & 1 evaluates to 1 (which Python treats as True in an if statement).If the bit was a 0, it evaluates to 0 (False)
        # res += 1: Whenever the isolated bit is a 1, your counter increments.
        res = 0
        for i in range(32):
            if n>>i & 1:
                res +=1
        
        return res