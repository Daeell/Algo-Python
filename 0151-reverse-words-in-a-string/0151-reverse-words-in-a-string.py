class Solution:
    def reverse(self, s: list, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        s = list(s)
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                self.reverse(s, start, i - 1)
                start = i + 1
        self.reverse(s, start, i)
        self.reverse(s, 0, len(s) - 1)

        return " ".join("".join(s).split())