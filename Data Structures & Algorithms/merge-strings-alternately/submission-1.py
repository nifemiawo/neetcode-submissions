class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        w1P = w2P = 0

        while w1P < len(word1) or w2P < len(word2):
            if w1P < len(word1):
                res.append(word1[w1P])

            if w2P < len(word2):
                res.append(word2[w2P])
            w1P += 1
            w2P += 1

        return "".join(res)