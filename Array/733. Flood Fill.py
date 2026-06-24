class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # recursive 

        source = image[sr][sc]

        def dfs(r,c):
            if (r < 0) or (r > len(image)-1) or (c < 0) or (c > len(image[0]) -1):
                return 
            if image[r][c] != source:
                return
            if image[r][c] == color:
                return

            image[r][c] = color

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        dfs(sr,sc)
        return image
        

# Both time and space complexity is O(n*m) where n is the number of rows and m is the number of columns in the image.
        
        