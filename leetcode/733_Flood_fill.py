'''
733. Flood Fill
Easy

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.
 
Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image == None or image[sr][sc]==color:
            return image #if there is no image or if the image is already the new color
        self.fillColor(image,sr,sc,image[sr][sc],color) #recursive function
        return image
    
    def fillColor(self,image,r,c,initial,color):
        if r<0 or r>=len(image) or c<0 or c>=len(image[0]) or image[r][c]!=initial:
            return 
            '''if the image cell is out of bound or not equal to the initial cell color (for initial 1 cell when trying to change the color of the right cell having 0 which is not equal to the initial color)'''
        image[r][c]=color #converts the color
        self.fillColor(image,r-1,c,initial,color) #up
        self.fillColor(image,r+1,c,initial,color) #down
        self.fillColor(image,r,c-1,initial,color) #left
        self.fillColor(image,r,c+1,initial,color) #right