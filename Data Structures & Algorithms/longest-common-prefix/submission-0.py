class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        

        for s in strs[1:]:
            i=0
            if s == "":
                return ""
            while i < len(longest) and i < len(s):
                if s[i] != longest[i]:
                    break
                i+=1
            longest = longest[:i]
        return longest

             