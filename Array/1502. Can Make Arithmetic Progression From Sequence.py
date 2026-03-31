class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        x = 0
        y = 1
        while y < len(arr):
            if arr[y] - arr[x] != diff:
                return False
            x = x + 1
            y = y + 1
        
        return True
        