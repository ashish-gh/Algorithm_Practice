# Question
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

 


from typing import List



class Solution:
    def rotate(self, matrix: List[List]):

        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r-l):
                top, bottom = i, i
                # store topleft
                top_left = matrix[top][l+i]
                # move bottom left into top left
                matrix[top][l+i]= matrix[bottom-i][l]

                # move bottom right into bottom left
                matrix[bottom-i][l]= matrix[bottom][r -i]

                # move top right into bottom right
                matrix[bottom][r-i]= matrix[top +i ][r]

                # move top left into top right
                matrix[top +i][r] = top_left
            
            l -=1
            r +=1
