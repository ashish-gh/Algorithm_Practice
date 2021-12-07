"""
we want to traverse to the string in backward directions.
and check if the current string if less than or greater than prior string(string before it 
since we are going in reverse order) 
if prior is greater than the current add else subtract
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        N = len(s)
        i = N -1
        output = 0
        while i >= 0:
            if i < N-1 and lookup[s[i]] < lookup[s[i +1]]:
                output -= lookup[s[i]]
            else:
                output += lookup[s[i]]
            i -= 1
        return output


sol = Solution()
print(sol.romanToInt("MDCXLIV"))

