class Solution(object):
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]

        if old == color:
            return image

        def dfs(r, c):
            if (0 <= r < len(image) and
                0 <= c < len(image[0]) and
                image[r][c] == old):

                image[r][c] = color

                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        dfs(sr, sc)
        return image