class Solution:
    all_lst = [
        ["I", 1], 
        ["IV", 4],
        ["V", 5],            
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000]
    ]

    def intToRoman(self, num: int) -> str:
        res =""
        for sym, val in reversed(self.all_lst):
            if num // val:
                count = num // val
                print(num, val, count)
                res += (sym * count)
                num = val % num
        return res
    def sol2(self, num: int):
        output = []
        for k, v in reversed(self.all_lst):
            while num > 0:
                if v <= num:
                    output.append(k)
                    num -= v
                else:
                    break
        return ''.join(output)


sol = Solution()
print(Solution().intToRoman(8))
print(sol.sol2(3))