class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        if word1 == word2:
            for char1, char2 in zip(word1, word2):
                merged += char1 + char2
                print(merged)
        else:
            for char1, char2 in zip(word1, word2):
                merged += char1 + char2
            diff = len(merged) // 2
            longer_word = word1 if len(word1) > len(word2) else word2
            substring = longer_word[diff:]
            merged += substring

        return merged
