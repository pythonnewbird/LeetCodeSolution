class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]
        queue = [(sr, sc)]
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        while queue:
            x, y = queue.pop(0)
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(image) and 0 <= ny < len(image[0]):
                    if image[nx][ny] != newColor and image[nx][ny] == oldColor:
                        image[nx][ny] = newColor
                        queue.append((nx, ny))
        return image