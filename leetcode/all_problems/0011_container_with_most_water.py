from typing import List


class Solution:
    # solution 1
    def max_area(self, height: List[int]) -> int:
        # store the left and the right pointers
        l, r = 0, len(height) - 1
        area = 0
        # while we are still in the bound calculate the ares
        while l < r:            
            # Calculate area
            # left - right is the widht 
            # minimum of height of l and height of r is the height and then multiply them to get area
            # max of area of previous and new area is the max area
            area = max(area,(r - l) * (min(height[l], height[r])))

            # if the height of left side is smaller increase the left pointer 
            # else decrese the right pointer            
            if height[l] < height[r]:
                l +=1
            else:
                r -=1
        return area
    

    # solution 2
    def area_two(self, height: List[int]) -> int:
        pass


if __name__ == "__main__":
    heights = [1,2,4,5]
    sl = Solution()
    print(sl.max_area(heights))


def cal_area(height):
    l, r = 0, len(height)-1
    while l < r:
        area = max(area,(l-r) * min(height[l] , height[r]))
        if height[l] < height[r]:
            l +=1
        else:
            r -=1
    return area