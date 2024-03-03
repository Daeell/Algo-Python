class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        xc1 = Counter(word1)
        xc2 = Counter(word2)
        checkClose = len(Counter(xc1.values()) - Counter(xc2.values())) == 0
        return xc1.keys() == xc2.keys() and checkClose