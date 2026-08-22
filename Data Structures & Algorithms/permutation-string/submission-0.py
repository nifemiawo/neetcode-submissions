class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map= defaultdict(int)
        s2Map = defaultdict(int)
        left=0
        k= len(s1)

        for char in s1:
            s1Map[char]+=1

        for right in range(len(s2)):
            s2Map[s2[right]]+=1

            if right-left+1 > k:
                s2Map[s2[left]]-=1
                if s2Map[s2[left]] ==0:
                    del s2Map[s2[left]]
                left+=1
            
            if right-left+1 ==k:
                if s1Map == s2Map:
                    return True
        
        return False

