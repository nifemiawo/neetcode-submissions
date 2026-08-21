class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1P = 0
        w2P =0
        ans = ""

        while w1P < len(word1) or w2P < len(word2):
            if w1P < len(word1):
                ans+=word1[w1P]
                w1P+=1


            if w2P < len(word2):
                ans+=word2[w2P]
                w2P+=1
        return ans

            