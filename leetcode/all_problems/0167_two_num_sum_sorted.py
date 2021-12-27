# Time complexity: O(n)
# Spacy complexity: O(1)
# Interview question in  [Amazon, ]

# Question: 
# Given an array is already sorted in ascending order, find two number such that they add to specific number
# The function should return indices such that the first index should be less than the second index

# Note:
# 1. Your index are not zero based 
# 2. Each input should have exactly one solution based.11

# Examples:
# nums = [2,7,9,11]
# return  = [1, 2]


from typing import List
class Solution:
    def two_number_sum_sorted(self, nums: List[int], target : int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum > target:
                r -=1
            elif cur_sum < target:
                l +=1
            else:
                return [l +1, r +1]
        return []


if __name__ == "__main__":
    sl = Solution()
    nums = [2,4,7,9,11,15]
    target = 9
    print(sl.two_number_sum_sorted(nums, target))
