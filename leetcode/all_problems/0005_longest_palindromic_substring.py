class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        for i, char in enumerate(s):
            # for odd cases
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                # while left and right pointer are in bound and 
                # while this is valid palindrome

                if (r-l-1) > res_len:
                    # the lenght of the palindrom is greater than the current palindrome length
                    # update the result
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -=1
                r +=1

            # even cases
            l, r = i, i+1
            while l >= 0 and r < len(res) and s[l] == s[r]:
                if (r - l - 1) > res_len:
                    res = s[l: r+1]
                    res_len = r - l + 1
                l -=1
                r +=1
        return res

#---
    def longestPalindrome_1(self, s):
        self.maxlen = 0
        self.start = 0

        for i in range(len(s)):
            self.expandFromCenter(s,i,i)
            self.expandFromCenter(s,i,i+1)
        return s[self.start:self.start+self.maxlen]
    

    def expandFromCenter(self,s,l,r):
        while l > -1 and r < len(s) and s[l] ==s[r]:
            l -= 1
            r += 1

        if self.maxlen < r-l-1:
            self.maxlen = r-l-1
            self.start = l + 1

