# class Solution:
#     def mySqrt(self, x: int) -> int:
#         n = 1

#         while n*n <= x:
#             n+=1
#         return n-1

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left,right = 1,x//2

        while left <= right:
            mid = (left+right)//2

            square = mid* mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right

# Use two pointer to do binary serch and time complexcity is log n 
        