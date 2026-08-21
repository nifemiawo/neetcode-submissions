class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp represents  can the first s[i] characters be built from i characters 

        dp = [False] * (len(s)+1)
        dp[0] = True
        wordDicts = set(wordDict)

        for i in range(1,len(s)+1):
            for j in range(i):
                if s[j:i] in wordDicts and dp[j]:
                    dp[i] = True
        
        return dp[len(s)]