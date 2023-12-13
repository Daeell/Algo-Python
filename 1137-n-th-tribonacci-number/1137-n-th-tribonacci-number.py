class Solution:
    def tribonacci(self, n: int) -> int:
        sequence = [0 for _ in range(n + 1)]
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        sequence[1], sequence[2] = 1, 1
        for i in range(3, n + 1):
            sequence[i] = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        return sequence[n]