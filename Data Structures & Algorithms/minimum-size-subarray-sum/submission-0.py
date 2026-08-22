class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        tot=0
        left=0
        minLen = 1000
        for right in range(len(nums)):
            tot+=nums[right]

            while tot >= target:
                tot-=nums[left]
                minLen = min(right-left+1,minLen)
                left+=1
                
        
        if minLen == 1000:
            return 0
        else:
            return minLen
