from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_one, len_two = len(str1), len(str2)
        gcd_len = gcd(len_one, len_two)
        
        def is_gcd(gcd_len):
            if len_one % gcd_len and len_two % gcd_len:
                return False
            else:
                l1, l2 = len_one // gcd_len, len_two // gcd_len
                base = str1[:gcd_len]
                return str1 == l1 * base and str2 == l2 * base

        for i in range(gcd_len, 0, -1):
            if is_gcd(i):
                return str1[:i]
            return ""