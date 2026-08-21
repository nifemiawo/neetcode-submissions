class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for c in s:
            s_freq[c] +=1
        

        for c in t:
            t_freq[c] +=1

        
        if t_freq== s_freq:
            return True
        else:
            return False

