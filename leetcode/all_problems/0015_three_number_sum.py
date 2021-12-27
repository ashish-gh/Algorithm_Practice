# Question
#

# Implementation
# 1. sort the input array
# 2. 

# Time complexity: O(n^2)
# Space complexity: O(1) or O(n) depends on the sorting algo used by the library



from typing import List


class Solution:
    def three_number_sum(self, numbers: List[int]) -> List[int]:
        res = []
        numbers.sort()
        for i, a in enumerate(numbers):
            # don't want to use the same value in the same position twice so
            # if the value is same as the previous value we don't want to use it
            if i > 0 and a == numbers[i -1]: continue

            # now implement the two pointer solution that is used in two sum solution 
            l, r = i + 1, len(numbers)- 1
            while l < r:
                cur_sum = a + numbers[l] + numbers[r]
                if cur_sum > 0:
                    r -=1
                elif cur_sum < 0:
                    l -=1
                else:
                    res.append([a,numbers[l] , numbers[r]])
                    l +=1   
                    while numbers[l] == numbers[l-1] and l < r:
                        l +=1
            return res

                
