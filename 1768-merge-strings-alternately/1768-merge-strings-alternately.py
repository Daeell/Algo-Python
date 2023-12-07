class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        for i in range(min(len(word1), len(word2))):
            merged_string += word1[i]
            merged_string += word2[i]

        merged_string += word2[len(word1):]
        merged_string += word1[len(word2):]
        return merged_string