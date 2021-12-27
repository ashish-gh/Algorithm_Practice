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
                matrix[bottom][r-1]= matrix[top +i ][r]

                # move top left into top right
                matrix[top +1][r] = top_left
            
            l -=1
            r +=1
