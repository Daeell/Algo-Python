class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getMaximumPalindrome(l, r):
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):
            odd = getMaximumPalindrome(i, i)
            even = getMaximumPalindrome(i, i+1)
            
            res = max(odd, even, res, key=len)
        return res